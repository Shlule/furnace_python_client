"""
defenition for hadlers for all the cli commands
"""

import os 
import asyncio
import subprocess
from concurrent import futures
from pprint import pprint
from pythonclient.check_query import CheckQuery
from pythonclient.core.config import Config
from pythonclient.core.context import Context
from pythonclient.utils.log import logger

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

def check_handler(check_name: str, dcc:str ,**kwargs) -> None:
    """
    Execute the check in the curren context
    """

    # find the path of the check

    config = Config()

    if kwargs.get("list", False):
        #just print the avaible check
        check_names = [check["name"] for check in config.checks]
        print("avaible checks: ")
        pprint(check_names)
        return
    
    if not check_name:
        logger.error("No action name provided")
        return
    
    furnace_context = Context.get()
    # must insert the dcc in context metadata here
    furnace_context.setDcc(dcc)
    furnace_context.start_services()

    check = CheckQuery
    

    print(kwargs)
    # print(Context.get())
    # context = Context.get()
    # context.setDcc(dcc)
    # context.start_services()
    
    # test.is_check_exist(check_name)

