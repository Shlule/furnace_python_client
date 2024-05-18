import asyncio
from typing import TYPE_CHECKING, Optional
from pythonclient.check_buffer import CheckBuffer
from pythonclient.utils.enums import CheckStatus
from pythonclient.core.context import Context
from pythonclient.core.config import Config

if TYPE_CHECKING:
    from pythonclient.core.event_loop import EventLoop
    from pythonclient.core.network.websocket import WebSocketConnection

class CheckQuery:
    """
    Initialize and execute a check
    """

    def __init__(self, name:str):
        self.name = name
        self.buffer =  CheckBuffer(name)
        context = Context.get()
        

        self.event_loop: EventLoop = context.event_loop
        self.ws_connection : WebSocketConnection = context.ws_connection

        self._task: Optional[asyncio.Task] = None

    async def execute_check_in_other_thread(self):

        print("je suis dans la function")
        await self.buffer.executor.run()



    def execute(self) -> None:
        self.buffer.status = CheckStatus.INITIALIZED

        # must call other async function to run the check( in an ) other thread
        # asynchronously
        print("bonjour")
        async def create_task():
            self._task = self.event_loop.loop.create_task(
                self.execute_check_in_other_thread()
            )
        return self.event_loop.register_task(create_task())
        # print(self.buffer.executor)
        # print(check)
        

        





        




