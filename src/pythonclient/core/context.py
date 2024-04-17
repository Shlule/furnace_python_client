
from __future__ import annotations

import asyncio
import os
import sys
import uuid
from concurrent import futures
from queue import Queue
from typing import TYPE_CHECKING, Any, Callable, Dict, ItemsView, KeysView, ValuesView

from pythonclient.core.event_loop import EventLoop
from pythonclient.core.network.websocket import WebSocketConnection

class Context:

    """
    Singleton-like class that keeps track of the current context
    This class should not be instanciated use the already instanciated object from this module
    or use the get() static method
    """
    def __init__(self) -> None:

        self.event_loop = EventLoop()
        self.ws_connection = WebSocketConnection('ws://127.0.0.1:3000', self.event_loop)
    
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
    
    


context = Context()

