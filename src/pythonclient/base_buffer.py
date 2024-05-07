from __future__ import annotations

import copy
import re
import uuid as unique_id
from dataclasses import dataclass, field, fields
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import dacite.config as dacite_config
import dacite.core as dacite
import jsondiff

T = TypeVar("T", bound="BaseBuffer")


@dataclass()
class BaseBuffer:
    """
    template class to construct a buffer, 
    """
    CHILD_NAME = "none"

    PRIVATE_FIELDS = ["outdated_cache", "serialized_data"]

    # Name of the buffer, must have no space and no special characters
    name: str = field(default= "Unnamed")
    # the name of the buffer, meant to display
    label: Optional[str] = field(compare=False, repr=False, default=None)
    #   childs in the buffer hierarchy of buffer
    children: Dict[str, BaseBuffer]= field(default_factory=dict)
    # Small explanation for the UI
    tooltip: Optional[str] = field(compare=False, repr=False, default=None)
    # A unique ID to help diferenciate multiple buffer
    uuid: str = field(default_factory=lambda:str(unique_id.uuid4()))

    # variable to keep tracking if the cache of this dataclass is outdated
    outdated_cache: bool = field(compare=False, repr=False, default=True)
    # variable to cache the data of the dataclass for the ui
    serialized_data: dict = field(compare=False, repr=False, default_factory=dict)


    def serialize(self, ignore_fields: List[str] =None):
        """
        Convert a buffer's data into an encodable JSON object ( a dict)
        """

        if not self.outdated_cache:
            return self.serialized_data
        if ignore_fields is None:
            ignore_fields = self.PRIVATE_FIELDS

        result = []

        for buffer_field in fields(self):
            if buffer_field.name in ignore_fields:
                continue
            if buffer_field.name == "children":
                children = getattr(self, buffer_field.name)
                children_value = {}
                for child_name, child in children.items():
                    children_value[child_name] = child.serialize()
                result.append((self.CHILD_NAME, children_value))
                continue
            result.append((buffer_field.name, getattr(self, buffer_field.name)))

        self.serialized_data = copy.deepcopy(dict(result))
        self.outdated_cache = False
        return self.serialized_data
    

    @property
    def child_type(self) -> Type[BaseBuffer]:
        return BaseBuffer
    
    

            


    

