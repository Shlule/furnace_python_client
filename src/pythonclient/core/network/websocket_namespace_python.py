from pythonclient.core.network.websocket_namespace import WebsocketNamespaceBase

class WebsocketNamespacePython(WebsocketNamespaceBase):
    

    async def on_connect(self):
        await super().on_connect()
        
        print(f"je suis dans on_connect du namespec python {self.namespace}")

        initialisation_data = {
            "context": "bonjour",
            "runningActions": "tout le monde",
        }

        await self.ws_connection.async_send(
            self.namespace, "initialization", initialisation_data
        )

        
    
