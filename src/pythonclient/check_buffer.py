from __future__ import annotations

import copy
import importlib
import os
import traceback
from contextlib import suppress
from dataclasses import dataclass, field, field
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from pythonclient.utils.enums import CheckStatus
from pythonclient.parameter_buffer import ParameterBuffer

import dacite.config as dacite_config
import dacite.core as dacite
import jsondiff

@dataclass
class CheckBuffer():
    """
    Store the data of a check, this class is data representation of a check
    """

    name: str = field(default="Unnamed")

    label: Optional[str] = field(compare=False, repr=False, default=None)

    status: CheckStatus = field(default=CheckStatus.UNCHECK, init=False)

    children: Dict[str, ParameterBuffer] = field(default_factory=dict)






    