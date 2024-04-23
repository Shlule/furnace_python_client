"""
defenition for hadlers for all the cli commands
"""

import os 
import asyncio
import subprocess
from concurrent import futures
from pprint import pprint
from src.pythonclient.core.config import Config

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
    """
    Execute the check in the curren context
    """

    # find the path of the check

    check = [check_name]
  

    test = Config()
    print(f"config:{test.checks}")

