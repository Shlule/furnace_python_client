"""
defenition for hadlers for all the cli commands
"""

import os 
import asyncio
import subprocess
from concurrent import futures
from pprint import pprint

def launch_handler(dcc: str, **kwargs) -> None:
    """
    Run the given command in the slected context
    """
    command = [dcc]
    arg_list = []
    print(command)

    subprocess.Popen(command, cwd=os.getcwd(), shell=True)

def checklist_handler():
    pass

def check_handler(check_name: str, **kwargs) -> None:
    print("je suis dans le check_handlers")
    pprint(kwargs)