from typing import TYPE_CHECKING
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

    async def execute(self) -> None:
        self.buffer.status = CheckStatus.INITIALIZED
        Config.get().is_check_exist(self.name)
        

        





        




