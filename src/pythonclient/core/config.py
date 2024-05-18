from __future__ import annotations

import contextlib
import copy
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from pathlib import Path

from pythonclient.utils.log import logger

# import dacite

# import pkg_resources
# from dacite import types


search_path = Optional[List[str]]

class Config:
    """ 
    utility class  that lazy loads and resolve configuration on demand
    """

    def __init__(self, checkRepo_search_path = None ):
        
        self.checkRepo_search_path = checkRepo_search_path
        if checkRepo_search_path is None:
            self.checkRepo_search_path = Config.get_default_checkRepo_search_path()


    def find_checks(self, search_path: List[str])->List[Dict[str,str]]:
        """
        find all config in the given paths
        """

        founded_check = []

        # get all file in the checkRepository folder in each search_path

        # for path in search_path:
        #     if not os.path.isdir(path):
        #         continue
        #     list_check_path = Path(path).glob('**/*.py')
        #     for check_path in list_check_path:
        #         check_name = check_path.stem
        #         if check_name == "__init__":
        #             continue
        #         founded_check.append({"name":check_name, "path": check_path})

        for path in search_path:
            checkRepo_path_list = Path(path).glob('**/checkRepository')
            for checkRepo_path in checkRepo_path_list:
                check_path_list = Path(checkRepo_path).glob('**/*.py')
                for check_path in check_path_list:
                    check_name = check_path.stem
                    module_path = check_path.parent
                    if check_name == "__init__":
                        continue
                    # relative to is a pathlib feature
                    premodule = module_path.relative_to(path)
                    module_parts = premodule.parts
                    module_base = ".".join(module_parts)
                    module = (f"{module_base}.{check_name}")

                    founded_check.append({"name": check_name, "module": module})
                    
        return founded_check
            
    
    def get_checks(self) -> List[Dict[str,str]]:
        return self.find_checks(
            [os.path.join(path) for path in self.checkRepo_search_path]
        )
    
            
    @property
    def checks(self) -> List[Dict[str,str]]:
        return self.get_checks()
    
    @staticmethod
    def get() -> Config:
        """
        Return a globaly instanciated config. This static method is just for conveniance
        """
        # Get the instance of Context created in this same module
        return getattr(sys.modules[__name__], "config")

    def is_check_exist(self, check_name:str):

        """
        prefer to return a real object if find it  compare to return bool
        """

        for check in self.checks:
            if check["name"] == check_name:
                logger.debug("found check: %s", check_name )
                return check
        logger.error(
            "could not resolve the check %s: The check does not exists", check_name
        )
        return None
       

        
    # def _load_config(self, checkRepo_path: str):
    #     """
    #     this function is for load all the checkRepository folder, 
    #     in a centralized file , containing the path of all CheckRepository folder
    #     """
    #     with open



    @staticmethod
    def get_default_checkRepo_search_path():
        
        """
        Get a list of path for searching the checkRepository folder
        from ENV variable and entryPont

        this is the default config object
        """

        checkRepo_search_path=[]

        env_config_path = os.getenv("FURNACE_ROOT_PACKAGES")
        if env_config_path is not None:
            checkRepo_search_path += env_config_path.split(os.pathsep)

        #Look for config search path in Furnace Config entry point

        # for entry_point in pkg_resources.iter_entry_points("furnace_check_config"):
        #     with contextlib.suppress(pkg_resources.DistributionNotFound):
        #         checkRepo_search_path += entry_point.load()
        # not avaible now

        return checkRepo_search_path
    
config = Config()

if __name__ == "__main__":
    test =Config()

