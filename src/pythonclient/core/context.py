
from __future__ import annotations

import asyncio
import os
import sys
import uuid
from concurrent import futures
from queue import Queue
from typing import TYPE_CHECKING, Any, Callable, Dict

from pythonclient.core.event_loop import EventLoop
from pythonclient.core.network.websocket import WebSocketConnection

class Context:

    def __init__(self) -> None:
        self.metadata: Dict[str,Any] = {"name": None, "uuid": str(uuid.uuid4()), "dcc": None}
        self.event_loop = EventLoop()
        self.ws_connection = WebSocketConnection('http://localhost:3000',self.metadata, self.event_loop)
    
    def start_services(self):
        self.event_loop.start()
        self.ws_connection.start()
    
    def stop_services(self):
        futures.wait([self.ws_connection.stop()], timeout=None)
        self.event_loop.stop()

    @staticmethod
    def get() -> Context:
        """
        return a globally instanciated context this static get is for conveniance
        """
        return getattr(sys.modules[__name__], "context")
    
    def setDcc(self, dcc) -> None:
        self.metadata["dcc"] = dcc 
    
    
    


context = Context()

