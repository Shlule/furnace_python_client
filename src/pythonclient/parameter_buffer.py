from pythonclient.base_buffer import BaseBuffer
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Type



@dataclass
class ParameterBuffer(BaseBuffer):
    """
    store the data of a parameter, this is a class representation of a parameters
    """
    name: str = field(default="Unnamed")

    type: Type = field(default=type(None))

    value : Any = field(default=None)

    # x:str

    # y:i


if __name__ == "__main__":
    from dacite import from_dict

    mydict = {'type': int,
              'value': 30,
              'name':"testParameterBuffer"}
    
    test = from_dict(ParameterBuffer,mydict)
