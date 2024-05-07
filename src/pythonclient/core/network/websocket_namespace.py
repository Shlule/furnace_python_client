"""
base class for all websocket namespaces
"""

from __future__ import annotations

import typing

import socketio
from typing import Any,Dict
from pythonclient.utils.log import logger

if typing.TYPE_CHECKING:
    from pythonclient.core.network.websocket import WebSocketConnection

class WebsocketNamespaceBase(socketio.AsyncClientNamespace):

    def __init__(self, namespace: str, context_data:Dict[str, Any], ws_connection: WebSocketConnection):
        super().__init__(namespace)
        self.context_data = context_data
        self.ws_connection = ws_connection
        self.url = ws_connection.url
    
    async def on_connect(self):
        """
        Register the dcc on furnace server on connection
        """
        logger.info("connected to %s on %s", self.url, self.namespace)
        pass

    async def on_disconnect(self):
        """
        Just Inform the user that furnace service is disconnected
        """
        logger.info("Disconnected from %s on %s", self.url, self.namespace)
        pass

