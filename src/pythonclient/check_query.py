from typing import TYPE_CHECKING
from pythonclient.check_buffer import CheckBuffer
from pythonclient.utils.enums import CheckStatus
from pythonclient.core.context import Context

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

    async def execute_checks(self) -> None:
        self.buffer.status = CheckStatus.INITIALIZED
        




