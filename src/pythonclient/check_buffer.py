from __future__ import annotations

import copy
import importlib
import os
import traceback
import pathlib
from contextlib import suppress
from dataclasses import dataclass, field, field
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from pythonclient.utils.enums import CheckStatus
from pythonclient.base_buffer import BaseBuffer
from pythonclient.core.config import Config
from pythonclient.parameter_buffer import ParameterBuffer
from pythonclient.utils.log import logger
from pythonclient.utils.converter import snake_to_pascal

if TYPE_CHECKING:
    from pythonclient.FurnaceCheckBase import FurnaceCheckBase

import dacite.config as dacite_config
import dacite.core as dacite
import jsondiff


@dataclass
class CheckBuffer(BaseBuffer):
    """
    Store the data of a check, this class is data representation of a check
    """

    name: str = field(default="Unnamed")

    label: Optional[str] = field(compare=False, repr=False, default=None)

    status: CheckStatus = field(default=CheckStatus.UNCHECK, init=False)

    #The path to the check Module
    path: str = field(default="")

    children: Dict[str, ParameterBuffer] = field(default_factory=dict)

    # The callable that will used when check is executed
    executor: FurnaceCheckBase = field(init=False)

    def __post_init__(self):
        super().__post_init__()

        module = Config.get().is_check_exist(self.name)
        if not module:
            logger.error(" cannot initialize the checkBuffer")
        self.path = module
        # auto load of the working check class
        # 
        # WARNING THIS IS IMPORT TO DECOMENT 
        self.executor = self._get_executor(module["module"])

    def _get_executor(self, module: str) -> FurnaceCheckBase:
        try: 

            """

            @ warning: cannot test if the executor is a subclass of FurnaceCheckBase, this cause circular import
            """

            split_module = module.split(".")
            module_path = ".".join(split_module[:-1])
            module_name = split_module[-1]

            # here thanks to import we can get the file path of the module
            module = importlib.import_module(module)
            importlib.reload(module)

            # by convention the check class name is in PascalCase
            # and the file name is in snake_case
            class_name = snake_to_pascal(module_name)
        
            executor = getattr(module, class_name)
            
            return executor
            

        except (
            ImportError,
            AttributeError,
            ModuleNotFoundError,
        ) as exception:
            logger.error("Invalid command path, skipping %s (%s)", module, exception)
            self.status = CheckStatus.INVALID
            if os.getenv("SILEX_LOG_LEVEL") == "DEBUG":
                traceback.print_tb(exception.__traceback__)

            return FurnaceCheckBase(self)



    