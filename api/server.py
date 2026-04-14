from fastapi import FastAPI, WebSocket

app = FastAPI()
clients = []

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    while True:
        await ws.receive_text()

async def broadcast(msg):
    for c in clients:
        await c.send_text(msg)
