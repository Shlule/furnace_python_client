import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print(sio.get_sid())
    print('connection established')
    await sio.emit("initialization", sio.sid)

@sio.on("check")
async def test_check(data):
    print(data)
    print(data["data"])
    exec(data["data"])
    
@sio.on('server message')
async def on_server_message(data):
    print('message received with: ', data)
    await sio.emit('my response', {'response': 'my response'})
    print("evenment myresponse envoye")

# @sio.event
# async def disconnect():
#     print('disconnected from server')

async def main():
    await sio.connect('http://localhost:3000', namespaces=(["/maya"]))
    await sio.wait()
    await sio.sleep(1)
    await sio.disconnect()

if __name__ == '__main__':
    asyncio.run(main())