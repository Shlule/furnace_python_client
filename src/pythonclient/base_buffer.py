import uuid as unique_id
from dataclasses import dataclass, field, fields
from typing import Any, Dict,List, Optional


@dataclass()
class BaseBuffer:
    """
    template class to construct a buffer, 
    """

    # Name of the buffer, must have no space and no special characters
    name: str = field(default= "Unnamed")
    # the name of the buffer, meant to display
    label: Optional[str] = field(compare=False, repr=False, default=None)
    # Small explanation for the UI
    tooltip: Optional[str] = field(compare=False, repr=False, default=None)
    # A unique ID to help diferenciate multiple buffer
    # uuid: str = field(default_factory=lambda:str(unique_id.uuid4()))

    

