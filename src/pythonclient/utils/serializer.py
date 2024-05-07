"""
helpers to encode personalized dataclass such as
checkBuffer, ParametersBuffer into JSON
"""
import uuid 

from pythonclient.check_buffer import CheckBuffer
from pythonclient.parameter_buffer import ParameterBuffer

def furnace_encoder(obj):
    """
    Helper to encode the check buffer to json
    """

    #convert uuid to hexadecimal
    if isinstance(obj, uuid.UUID):
        return obj.hex
    
    if isinstance(obj, (CheckBuffer, ParameterBuffer)):
        return obj.serialize()