import functools
import logging
import inspect
from typing import Any, Dict

from check_buffer import CheckBuffer

from pythonclient.utils.enums import CheckStatus

class FurnaceCheckBase:
    
    def __init__(self, name:str, check_buffer: CheckBuffer) -> None:
        
        self.name: str = name
        self.check_buffer = check_buffer
        self.type: str = type
        inheritance_tree = inspect.getmro(type(self))

        #merge the parameters of inherited trees
        self.parameters = {}
        # take all execpt the last one because always return object class 
        for inherited_class in  inheritance_tree[::-1]:
            if not hasattr(inherited_class,"parameters"):
                continue
            class_parameters = getattr(inherited_class, "parameters")
            if isinstance(class_parameters, dict):
                self.parameters.update(class_parameters)


    
    async def run(self,parameters: Dict[str,Any], ) -> Any:
        raise NotImplementedError(
            "this command does not have any execution function"
        )        
    

    # def is_valid_parameters(self, parameters, logger: logging.Logger) -> bool:
    #     """
    #     Check the if the input kwargs are valid accoring to the parameters list
    #     and conform it if nessesary
    #     """
    #     for parameters_name, parameter_buffer in self.check_buffer


    @staticmethod
    def conform_command():

        def decorator_conform_command(func):
            @functools.wraps(func)
            async def wrapper_conform_command(check: FurnaceCheckBase, *args, **kwargs)->None:
                print(f"kwargs: {kwargs}")
                print(f"args: {args}")

                # output = await func(*args, **kwargs)
                # return output
            return wrapper_conform_command
        return decorator_conform_command


    async def fix(self):
        pass

if __name__ == "__main__":
    check_buffer = CheckBuffer()
    test = FurnaceCheckBase("test", check_buffer)
    print(test)