from __future__ import annotations

import copy
import importlib
import os
import traceback
from contextlib import suppress
from dataclasses import dataclass, field, field
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from pythonclient.utils.enums import CheckStatus

import dacite.config as dacite_config
import dacite.core as dacite
import jsondiff

@dataclass
class CheckBuffer():
    """
    Store the data of a check
    """

    name: str = field(default="unnamed")

    label: Optional[str] = field(compare=False, repr=False, default=None)

    status: CheckStatus = field(default=CheckStatus.UNCHECK, init=False)




    