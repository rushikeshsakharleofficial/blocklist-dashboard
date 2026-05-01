from fastapi import FastAPI,WebSocket
from .blacklist_checker import check_ip

app=FastAPI()
clients=[]

@app.websocket("/ws")
async def ws(ws:WebSocket):
    await ws.accept()
    clients.append(ws)
    while True:
        data=await ws.receive_json()
        ip=data.get("ip")
        res=check_ip(ip)
        for c in clients:
            await c.send_json({"ip":ip,"results":res})
