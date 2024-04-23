from dataclasses import dataclass, field, fields
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

class test:
    def __init__(self, name: str):
        self.name = name


@dataclass
class testBuffer():
    """
    Store state of an action
    """

    name: str = field(default= "unnamed")

    label:str = field(default=None)

    tooltip: Optional[str] = field(compare=False, repr=False, default=None)

    test:bool = field(default=None)


if __name__ == "__main__":
    test1 = testBuffer()
    print(test1)

    test2 = testBuffer("none")
    print(test2)

    fieldlist = ["none", "bonjour", False, False]
    test3 = testBuffer(*fieldlist)
    print(*fieldlist)
    print(test3)

    fieldDict = {"name": "none",
                 "test": False,
                 "tooltip": 30,
                 "label": "bonjour",}
    
    print(**fieldDict)
    test4 = testBuffer(**fieldDict)
    print(test4)

    