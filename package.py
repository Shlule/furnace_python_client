name = "furnace_python_client"
timestamp = 0 
version = "dev.0.0.1"

authors = ["Shlule"]

vcs = 'git'

description = """
    set of module to excute check on DCC 
"""

def commands():

    env.PYTHONPATH.append("{root}")
    env.FURNACE_CHECK_CONFIG.prepend("{root}/src/pythonclient/checkRepository")

    parserpath = "src.pythonclient.cli.parser"
    if "houdini" in request:
        alias("furnace", f"hython -m {parserpath}")
                
    if "maya" in request:
        alias("furnace", f"mayapy -m {parserpath}")





# def requires():
#     if "furnace_houdini" in request:
#         return[f"houdini","maya"]
#     if "furnace_maya"in request:
#         return["maya"]

          

