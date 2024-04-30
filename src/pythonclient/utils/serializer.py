"""
helpers to encode personalized dataclass such as
checkBuffer, ParametersBuffer into JSON
"""

from pythonclient.check_buffer import CheckBuffer
from pythonclient.parameter_buffer import ParameterBuffer

def furnace_encoder(obj):
    """
    Helper to encode the check buffer to json
    """