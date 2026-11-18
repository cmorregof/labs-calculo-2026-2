import requests, pandas as pd, datetime as dt, time
U="https://servapibi.xm.com.co/"
def _post(kind, body):
    for i in range(4):
        try:
            r=requests.post(U+kind,json=body,timeout=90)
            if r.status_code==200: return r.json()
        except Exception as e: err=e
        time.sleep(2)
    raise RuntimeError(f"XM no respondió: {body}")
def diario(metric, entity, ini, fin, filtro=None):
    """Serie diaria [ini, fin] de una métrica DailyEntities. Devuelve fecha, nombre, valor."""
    ini=pd.Timestamp(ini); fin=pd.Timestamp(fin); out=[]
    a=ini
    while a<=fin:
        b=min(a+pd.Timedelta(days=29),fin)
        body={"MetricId":metric,"StartDate":str(a.date()),"EndDate":str(b.date()),"Entity":entity}
        if filtro: body["Filter"]=filtro
        j=_post("daily",body)
        for it in j.get("Items",[]):
            for e in it["DailyEntities"]:
                out.append((it["Date"],e.get("Name"),e.get("Value")))
        a=b+pd.Timedelta(days=1)
    return pd.DataFrame(out,columns=["fecha","nombre","valor"])
def horario(metric, entity, ini, fin, filtro=None):
    """Serie horaria: una fila por hora (hora = 0..23, inicio del periodo)."""
    ini=pd.Timestamp(ini); fin=pd.Timestamp(fin); out=[]
    a=ini
    while a<=fin:
        b=min(a+pd.Timedelta(days=29),fin)
        body={"MetricId":metric,"StartDate":str(a.date()),"EndDate":str(b.date()),"Entity":entity}
        if filtro: body["Filter"]=filtro
        j=_post("hourly",body)
        for it in j.get("Items",[]):
            for e in it["HourlyEntities"]:
                v=e["Values"]
                for h in range(1,25):
                    x=v.get(f"Hour{h:02d}")
                    out.append((it["Date"],h-1,v.get("code") or e.get("Name"),None if x in (None,"") else float(x)))
        a=b+pd.Timedelta(days=1)
    return pd.DataFrame(out,columns=["fecha","hora","nombre","valor"])
