from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Electron app</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <p>The app has been running for <span id='time-counter'>0</span> seconds.</p>        
        <script>
            var ws = new WebSocket("ws://localhost:8000/counter");
            ws.onmessage = function(event) {                
                document.getElementById('time-counter').innerText = event.data
            };
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/counter")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cnt = 0
    while True:
        await asyncio.sleep(1)
        cnt += 1        
        await websocket.send_text(f"{cnt}")
