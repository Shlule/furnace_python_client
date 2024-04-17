from __future__ import annotations

import contextlib
import copy
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


search_path = Optional[List[str]]

class Config:
    """ 
    utility class  that lazy loads and resolve configuration on demand
    """

    def __init__(self, config_se) -> None:
        pass