# # class WebsocketConnection:

# #     MESSAGE_CALLBACK_TIEMOUT = 1

# #     def __init__(self, url:str):
# #         self.url = url

# import os
# from pprint import pprint 

# import maya.standalone

# maya.standalone.initialize()

# import maya.cmds
# print("hello")

# def print_all_env_variables():
#     for key, value in os.environ.items():
#         pprint(f"{key}: {value}")

# # Call the function to print all environment variables
# print_all_env_variables()

from __future__ import annotations

import asyncio
import json
from concurrent import futures
from typing import TYPE_CHECKING, Any, Dict
from pythonclient.core.event_loop import EventLoop
from pythonclient.utils.log import logger
import socketio
from socketio.exceptions import ConnectionError

class WebSocketConnection:
    """
    Websocket client that connect the the given url
    and receive and handle the incomming messages
    """

    #: How long to wait for a confirmation fom every messages sent
    MESSAGE_CALLBACK_TIEMOUT = 1

    def __init__(self, url:str, event_loop: EventLoop):
        self.url = url
        self.socketio = socketio.AsyncClient()
        self.event_loop = event_loop


    @property
    def is_running(self):
        return self.socketio.connected 
    
    async def _connect_socketio(self) -> None:
        try:
            await asyncio.wait_for(self.socketio.connect(self.url), 2)
        except (asyncio.TimeoutError, ConnectionError):
            logger.warning(
                "Conection with the websocket server could not be establish"
            )
        
    
    async def _disconnect_socketio(self) -> None:
        await self.socketio.disconnect()

    def start(self) -> futures.Future:
        #initialize event_loop task's and run it
        if self.is_running:
            logger.warning(" could not start websocket connection: the connection is already running")
            future: futures.Future = futures.Future()
            future.set_result(None)
            return future
        
        future = self.event_loop.register_task(self._connect_socketio())
        futures.wait([future])
        return future
    
    def stop(self) -> futures.Future:
        """
        Ask to all the event loop's tasks to stop
        if there is one running
        """
        if not self.is_running:
            future: futures.Future = futures.Future()
            future.set_result(None)
            return future
        
        future = self.event_loop.register_task(self._disconnect_socketio())
        futures.wait([future])
        return future
    def send(self , namespace: str , ev)


