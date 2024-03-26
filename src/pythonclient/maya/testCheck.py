from typing import str
from FurnaceCheckBase import FurnaceCheckBase

from maya import cmds

class testCheck(FurnaceCheckBase):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    
    async def run(self):
        object = cmds.ls(geometry=True)
        print(object)

    async def fix(self):
        print("hello")