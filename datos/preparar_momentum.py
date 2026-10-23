#!/usr/bin/env python3
"""
preparar_momentum.py — Congela los datos del Lab 2 (*El partido que se acumula*):
del evento a evento crudo de StatsBomb a la tasa de dominio minuto a minuto.

Curso de Cálculo Integral, UNAL Manizales (Carlos Manuel Orrego Franco).
Es a este laboratorio lo que agregar_londres.py fue al L1: no me crean — reprodúzcanlo.

Uso:
    python3 preparar_momentum.py                       # final Mundial 2022 (Argentina–Francia)
    python3 preparar_momentum.py --partido copa2024    # final Copa América 2024 (Argentina–Colombia)
    python3 preparar_momentum.py --match-id 3869519    # cualquier partido por id de StatsBomb
    python3 preparar_momentum.py --listar 43 106       # lista los partidos de una competición/temporada
    python3 preparar_momentum.py --memoria 5 --grafica # otra memoria, y además la gráfica

Datos: StatsBomb Open Data (github.com/statsbomb/open-data), descargados al vuelo.
Salidas (carpeta actual, o --salida): eventos_<nombre>.csv, momentum_<nombre>.csv
(y momentum_<nombre>.png con --grafica). El CSV de momentum NO trae la acumulada D(x):
construirla es el trabajo de la sesión 1.

LA RECETA (esto es lo que un estudiante debe poder discutir):
  1. Cada evento del partido recibe "puntos de peligro" según su tipo y su zona:
        remate ............ 1 + 5·xG   (+2 si fue gol)
        pase/conducción que termina en el último cuarto (x >= 90) ... 0.15
        pase/conducción que termina dentro del área ................ +0.40
        regate completado ........................................... 0.30
        falta recibida en el último cuarto .......................... 0.20
        tiro de esquina ............................................. 0.30
     La tanda de penales (periodo 5) se excluye: no hay juego que acumular.
  2. Se suman los puntos de cada equipo por minuto corrido: tiempo real de juego, con los
     descuentos, de modo que un partido con prórroga dura ~140 minutos corridos.
  3. momentum_bruto[k] = peligro_local[k] − peligro_visitante[k]  (puntos de peligro / minuto)
  4. Se suaviza con una media móvil exponencial de "memoria" τ minutos:
        m[k] = (1 − λ)·m[k−1] + λ·r[k],  λ = 1/τ.
     El resultado m(t) es una función ESCALONADA: constante en cada minuto.
  5. El dominio acumulado hasta el minuto x es D(x) = ∫_0^x m(t) dt = Σ_{k<x} m[k]·1.
Todo lo anterior es UNA receta, no LA receta: los pesos, la zona y la memoria son decisiones.
"""
import argparse, json, os, sys, urllib.request

RAW = "https://raw.githubusercontent.com/statsbomb/open-data/master/data"

PARTIDOS = {           # nombre corto -> (match_id, comp_id, season_id, etiqueta)
    "final2022":  (3869685, 43, 106, "Final Mundial 2022 — Argentina 3–3 Francia (pen. 4–2)"),
    "semi2022":   (3869519, 43, 106, "Semifinal Mundial 2022 — Argentina 3–0 Croacia"),
    "cuartos2022":(3869321, 43, 106, "Cuartos Mundial 2022 — Países Bajos 2–2 Argentina"),
    "copa2024":   (3943077, 223, 282, "Final Copa América 2024 — Argentina 1–0 Colombia"),
    "semicopa2024":(3942852, 223, 282, "Semifinal Copa América 2024 — Uruguay 0–1 Colombia"),
}

PESOS = dict(remate_base=1.0, remate_xg=5.0, gol=2.0, ultimo_cuarto=0.15,
             area=0.40, regate=0.30, falta=0.20, corner=0.30)


def descargar(url, destino):
    if not os.path.exists(destino):
        print(f"  descargando {url}")
        urllib.request.urlretrieve(url, destino)
    with open(destino, encoding="utf-8") as f:
        return json.load(f)


def listar(comp_id, season_id, cache):
    m = descargar(f"{RAW}/matches/{comp_id}/{season_id}.json", os.path.join(cache, f"matches_{comp_id}_{season_id}.json"))
    for x in sorted(m, key=lambda z: z["match_date"]):
        print(f'{x["match_id"]}  {x["match_date"]}  {x["home_team"]["home_team_name"]:>22} {x["home_score"]}-{x["away_score"]} '
              f'{x["away_team"]["away_team_name"]:<22} {x["competition_stage"]["name"]}')


def puntos_de_peligro(ev):
    """Puntos de peligro de un evento según la receta del curso (0 si no cuenta)."""
    tipo = ev["type"]["name"]
    p = 0.0
    if tipo == "Shot":
        xg = ev.get("shot", {}).get("statsbomb_xg", 0.0) or 0.0
        gol = ev.get("shot", {}).get("outcome", {}).get("name") == "Goal"
        p = PESOS["remate_base"] + PESOS["remate_xg"] * xg + (PESOS["gol"] if gol else 0)
    elif tipo in ("Pass", "Carry"):
        d = ev.get("pass") if tipo == "Pass" else ev.get("carry")
        fin = (d or {}).get("end_location")
        if tipo == "Pass" and (d or {}).get("outcome"):      # pase incompleto: no cuenta
            fin = None
        if tipo == "Pass" and (d or {}).get("type", {}).get("name") == "Corner":
            p += PESOS["corner"]
        if fin and fin[0] >= 90:
            p += PESOS["ultimo_cuarto"]
            if fin[0] >= 102 and 18 <= fin[1] <= 62:
                p += PESOS["area"]
    elif tipo == "Dribble" and ev.get("dribble", {}).get("outcome", {}).get("name") == "Complete":
        p = PESOS["regate"]
    elif tipo == "Foul Won" and ev.get("location", [0])[0] >= 90:
        p = PESOS["falta"]
    return p


def codigo(equipo):
    """Argentina -> arg, France -> fra: tres letras para nombrar columnas."""
    import unicodedata
    s = unicodedata.normalize("NFKD", equipo).encode("ascii", "ignore").decode()
    return s.replace(" ", "")[:3].lower()


def procesar(match_id, memoria, cache, salida, nombre, etiqueta):
    eventos = descargar(f"{RAW}/events/{match_id}.json", os.path.join(cache, f"events_{match_id}.json"))
    eventos = [e for e in eventos if e["period"] <= 4]          # sin penales
    equipos = []
    for e in eventos:
        n = e["team"]["name"]
        if n not in equipos:
            equipos.append(n)
    local, visita = equipos[0], equipos[1]

    # --- minuto corrido: cada periodo empieza donde terminó el anterior ---
    fin_periodo, offset = {}, {}
    for e in eventos:
        t = e["minute"] + e["second"] / 60
        fin_periodo[e["period"]] = max(fin_periodo.get(e["period"], 0), t)
    inicio_nominal = {1: 0, 2: 45, 3: 90, 4: 105}
    acumulado = 0.0
    for p in sorted(fin_periodo):
        offset[p] = acumulado - inicio_nominal[p]
        acumulado += fin_periodo[p] - inicio_nominal[p]
    T = int(acumulado) + 1

    filas, pel = [], {local: [0.0] * T, visita: [0.0] * T}
    goles = []
    for e in eventos:
        t = e["minute"] + e["second"] / 60 + offset[e["period"]]
        k = min(int(t), T - 1)
        p = puntos_de_peligro(e)
        pel[e["team"]["name"]][k] += p
        tipo = e["type"]["name"]
        xg = e.get("shot", {}).get("statsbomb_xg", "") if tipo == "Shot" else ""
        gol = int(tipo == "Shot" and e.get("shot", {}).get("outcome", {}).get("name") == "Goal")
        if gol:
            goles.append((t, e["team"]["name"], e["player"]["name"], e["minute"] + 1))
        loc = e.get("location") or ["", ""]
        filas.append((e["period"], e["minute"], e["second"], round(t, 3), e["team"]["name"], tipo, loc[0], loc[1], xg, gol, round(p, 3)))

    # --- momentum bruto y suavizado (escalonada por minuto) ---
    lam = 1.0 / memoria
    bruto = [pel[local][k] - pel[visita][k] for k in range(T)]
    m = [0.0] * T
    for k in range(T):
        m[k] = lam * bruto[k] if k == 0 else (1 - lam) * m[k - 1] + lam * bruto[k]
    D = [0.0] * (T + 1)                       # D(x) en los enteros x = 0..T
    for k in range(T):
        D[k + 1] = D[k] + m[k] * 1.0          # ∫ de una escalonada: base 1 minuto por altura

    os.makedirs(salida, exist_ok=True)
    import csv
    with open(os.path.join(salida, f"eventos_{nombre}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["periodo", "minuto", "segundo", "t_corrido", "equipo", "tipo", "x", "y", "xg", "gol", "peligro"]); w.writerows(filas)
    with open(os.path.join(salida, f"momentum_{nombre}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["minuto", f"peligro_{codigo(local)}", f"peligro_{codigo(visita)}", "momentum_bruto", "momentum"])
        for k in range(T):
            w.writerow([k, round(pel[local][k], 3), round(pel[visita][k], 3), round(bruto[k], 3), round(m[k], 4)])

    # --- resumen ---
    kmax_m = max(range(T), key=lambda k: m[k]); kmin_m = min(range(T), key=lambda k: m[k])
    xmax_D = max(range(T + 1), key=lambda k: D[k]); xmin_D = min(range(T + 1), key=lambda k: D[k])
    print(f"\n{etiqueta}\n  equipos: {local} (arriba, +) vs {visita} (abajo, −); eventos: {len(filas)}; minutos: {T}")
    print(f"  dominio neto  ∫_0^{T} m = {D[T]:+.2f} puntos de peligro")
    print(f"  m máxima {m[kmax_m]:+.2f} en el minuto {kmax_m};  m mínima {m[kmin_m]:+.2f} en el minuto {kmin_m}")
    print(f"  D máxima {D[xmax_D]:+.2f} en x = {xmax_D};  D mínima {D[xmin_D]:+.2f} en x = {xmin_D}")
    cortes = [0] + [int(round(offset[p] + inicio_nominal[p])) for p in sorted(offset) if p > 1] + [T]
    for i in range(len(cortes) - 1):
        a, b = cortes[i], cortes[i + 1]
        print(f"  tiempo {i+1}: ∫_{a}^{b} m = {D[b]-D[a]:+.2f}  (promedio {(D[b]-D[a])/(b-a):+.3f} por minuto)")
    for t, eq, jug, mn in goles:
        print(f"  gol min {mn:3d} (t corrido {t:6.2f})  {eq:12s} {jug}")
    return dict(local=local, visita=visita, T=T, m=m, D=D, goles=goles, cortes=cortes, etiqueta=etiqueta, memoria=memoria)


def graficar(r, ruta):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    T, m, D = r["T"], np.array(r["m"]), np.array(r["D"])
    t = np.arange(T + 1)
    m_esc = np.append(m, m[-1])                      # escalonada: valor constante en [k, k+1)
    c_loc, c_vis, ink, grid = "#2F6DB5", "#C9573C", "#333333", "#DDDDDD"

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7.2), sharex=True, gridspec_kw=dict(hspace=0.12))
    for ax in (ax1, ax2):
        ax.grid(True, color=grid, linewidth=0.6); ax.set_axisbelow(True)
        for s in ("top", "right"): ax.spines[s].set_visible(False)
        for x in r["cortes"][1:-1]: ax.axvline(x, color="#999999", linewidth=0.8, linestyle=":")
    ax1.fill_between(t, np.maximum(m_esc, 0), 0, step="post", color=c_loc, alpha=0.85, linewidth=0)
    ax1.fill_between(t, np.minimum(m_esc, 0), 0, step="post", color=c_vis, alpha=0.85, linewidth=0)
    ax1.step(t, m_esc, where="post", color=ink, linewidth=0.8)
    ax1.axhline(0, color=ink, linewidth=0.8)
    ax1.set_ylabel("momentum  m(t)\n[puntos de peligro / min]")
    ax1.set_title(f"{r['etiqueta']}\n{r['local']} domina arriba (+), {r['visita']} domina abajo (−); memoria {r['memoria']} min", fontsize=11, loc="left", pad=14)
    ymax = float(np.abs(m).max()) * 1.15
    for i, (tg, eq, jug, mn) in enumerate(r["goles"]):
        col = c_loc if eq == r["local"] else c_vis
        ax1.plot([tg], [ymax * 0.92], marker="v", color=col, markersize=9)
        tk = jug.split(); apellido = tk[-2] if len(tk) > 2 else tk[-1]
        if len(tk) > 3 and tk[-3].lower() in ("di", "de", "da", "van", "von", "del"):
            apellido = tk[-3] + " " + apellido
        ax1.annotate(f"{apellido} {mn}'", (tg, ymax * 0.92), textcoords="offset points", xytext=(0, 8 + 11 * (i % 2)), ha="center", fontsize=8, color=ink)
    ax1.set_ylim(-ymax, ymax * 1.28)

    ax2.plot(t, D, color=ink, linewidth=2)
    ax2.fill_between(t, D, 0, where=D >= 0, color=c_loc, alpha=0.18, linewidth=0)
    ax2.fill_between(t, D, 0, where=D < 0, color=c_vis, alpha=0.18, linewidth=0)
    ax2.axhline(0, color=ink, linewidth=0.8)
    xM = int(np.argmax(D)); xm = int(np.argmin(D))
    ax2.plot([xM], [D[xM]], "o", color=c_loc, markersize=8)
    ax2.annotate(f"máx D = {D[xM]:+.1f} en x={xM}", (xM, D[xM]), textcoords="offset points", xytext=(8, 6), fontsize=9)
    if xm > 0:
        ax2.plot([xm], [D[xm]], "o", color=c_vis, markersize=8)
        ax2.annotate(f"mín D = {D[xm]:+.1f} en x={xm}", (xm, D[xm]), textcoords="offset points", xytext=(8, -14), fontsize=9)
    ax2.set_ylabel("dominio acumulado\nD(x) = ∫₀ˣ m(t) dt  [puntos]")
    ax2.set_xlabel("minuto corrido del partido (prórroga incluida, penales excluidos)")
    ax2.set_xlim(0, T)
    ax2.text(0.99, 0.04, f"D({T}) = {D[T]:+.1f}", transform=ax2.transAxes, ha="right", fontsize=10)
    fig.savefig(ruta, dpi=160, bbox_inches="tight")
    print(f"  gráfica guardada en {ruta}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--partido", default="final2022", choices=sorted(PARTIDOS), help="nombre corto del partido")
    ap.add_argument("--match-id", type=int, help="id de StatsBomb (ignora --partido)")
    ap.add_argument("--etiqueta", default=None, help="título para --match-id")
    ap.add_argument("--memoria", type=float, default=3.0, help="memoria τ del suavizado, en minutos (λ = 1/τ)")
    ap.add_argument("--listar", nargs=2, metavar=("COMP_ID", "SEASON_ID"), help="lista partidos disponibles y termina (Mundial 2022: 43 106; Copa América 2024: 223 282; Euro 2024: 55 282)")
    ap.add_argument("--cache", default="cache"); ap.add_argument("--salida", default=".")
    ap.add_argument("--grafica", action="store_true", help="además guarda la gráfica de m(t) y D(x)")
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    if a.listar:
        listar(*a.listar, a.cache); sys.exit()
    if a.match_id:
        mid, nombre, etiqueta = a.match_id, str(a.match_id), a.etiqueta or f"StatsBomb match {a.match_id}"
    else:
        mid, _, _, etiqueta = PARTIDOS[a.partido]; nombre = a.partido
    r = procesar(mid, a.memoria, a.cache, a.salida, nombre, etiqueta)
    if a.grafica:
        graficar(r, os.path.join(a.salida, f"momentum_{nombre}.png"))
