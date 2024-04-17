import asyncio
import socketio
from pythonclient.core.network.websocket import WebSocketConnection
from pythonclient.core.event_loop import EventLoop

# sio = socketio.AsyncClient()

# @sio.event
# async def connect():
#     print(sio.get_sid())
#     print('connection established')
#     await sio.emit("initialization", sio.sid)

# @sio.on("check")
# async def test_check(data):
#     print(data)
#     print(data["data"])
#     exec(data["data"])
    
# @sio.on('server message')
# async def on_server_message(data):
#     print('message received with: ', data)
#     await sio.emit('my response', {'response': 'my response'})
#     print("evenment myresponse envoye")

# @sio.event
# async def disconnect():
#     print('disconnected from server')
event_loop = EventLoop()
ws_connection = WebSocketConnection("http://localhost:3000", event_loop)

def start_services():
    event_loop.start() 
    ws_connection.start() 

async def main():
    # test = WebsocketNamespacePython("/maya",)
    # await sio.register_namespace(web)
    # await sio.connect('http://localhost:3000', namespaces=(["/maya"]))
    # await sio.wait()
    # await sio.sleep(1)
    # await sio.disconnect()
    event_loop = EventLoop()
    ws_connection = WebSocketConnection("http://localhost:3000", event_loop)

    event_loop.start()
    await asyncio.sleep(1)
    ws_connection.start()


if __name__ == '__main__':
    # asyncio.run(main())
    start_services()
    # from pythonclient.core.context import Context

    # Context.get().start_services()