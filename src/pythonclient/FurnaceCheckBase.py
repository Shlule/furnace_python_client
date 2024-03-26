from typing import str

class FurnaceCheckBase:
    
    def __init__(self, name: str, type: str) -> None:
        
        name: str = self.name
        status: str = " uncheck"
        type: str = self.type

    
    async def run(self):
        pass

    async def fix(self):
        pass
