# class WebsocketConnection:

#     MESSAGE_CALLBACK_TIEMOUT = 1

#     def __init__(self, url:str):
#         self.url = url

import os
from pprint import pprint 

import maya.standalone

maya.standalone.initialize()

import maya.cmds
print("hello")

def print_all_env_variables():
    for key, value in os.environ.items():
        pprint(f"{key}: {value}")

# Call the function to print all environment variables
print_all_env_variables()