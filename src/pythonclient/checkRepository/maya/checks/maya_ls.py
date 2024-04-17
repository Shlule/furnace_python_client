import typing 
import os
import asyncio

from pythonclient.FurnaceCheckBase import FurnaceCheckBase

class listObject(FurnaceCheckBase):
    
    """
    List all object of the asked type
    """

    async def run(self, parameters):
        print(parameters)

if __name__ == "__main__":
    test = listObject("listobject")
    asyncio.run(test.run(parameters="test"))