name = "furnace_python_client"
timestamp = 0 
version = "dev.0.0.1"

authors = ["Shlule"]

vcs = 'git'

description = """
    set of module to excute check on DCC 
"""

requires= [
    "dacite"
]

def conform_requires(require_list):
    conformed_requires = []
    for require in require_list:
        conformed = require.replace("-", "_").lower()
        conformed_requires.append(conformed)
    return conform_requires


def commands():

    import sys
    import os
    import tomllib
    import re

    print(f"sys.version_info: {sys.version_info}")

    env.PYTHONPATH.append("{root}/src")
    env.FURNACE_CHECK_CONFIG.prepend("{root}/src/pythonclient/checkRepository")


    parserpath = "pythonclient.cli.parser"
    alias("furnace", f"python -m {parserpath}")



@late()
def requires():
    import os
    import tomllib
    import re

    with open("D:/rez/Furnace_packages/furnace/furnace_python_client/dev.0.0.1/pyproject.toml","rb") as f:
        data = tomllib.load(f)
        dependencies = data["project"]["dependencies"]
        conformed_dependencies =[]
        for require  in dependencies:
            without_bracet = re.sub(r'\[.*?]','',require)
            conformed = without_bracet.replace("-","_").lower()
            # print(conformed)
            conformed_dependencies.append(conformed)

#     return [
#     "python_socketio",
#     "logzero",
#     # "argparse",
#     "dacite",
#     "jsondiff",
#     # "setuptools>=69.5.1",
# ]
    return conformed_dependencies
    


# def requires():
#     if "furnace_houdini" in request:
#         return[f"houdini","maya"]
#     if "furnace_maya"in request:
#         return["maya"]

          

