"""
    entryPoint for thr CLI tools of Furnace
"""
import argparse
from typing import Dict, Optional, Callable

from src.pythonclient.cli import handlers

def main(handlers_mapping: Optional[Dict[str,Callable]] = None):
    """
    parse the given arguments and call the appropriate handler

    """

    HANDLERS_MAPPING= {
        "checklist": handlers.checklist_handler,
        "check": handlers.check_handler,
        "launch": handlers.launch_handler,
    }
    if handlers_mapping:
        HANDLERS_MAPPING.update(handlers_mapping)

    execution_parser = argparse.ArgumentParser(add_help= False)
    execution_parser.add_argument(
        "--list",
        "-l",
        default= False,
        help="List the avaible option for the subcommand in the context",
        action="store_true",
    )

    parser = argparse.ArgumentParser(
        prog="furnace", description= "CLI for furnace sanitychecker ecosystem" 
    )
    
    subparsers = parser.add_subparsers(
        help="the action to perform under the given context",
        dest="subcommand"
    )

    check_parser = subparsers.add_parser(
        "check",
        help="Execute the given check in the context",
    )

    checklist_parser = subparsers.add_parser(
        "checklist",
        help="Execute the given checklist in the context",
    )

    launcher_parser = subparsers.add_parser(
        "launch",
        help="Launch the given program in the context",
    )

    check_parser.add_argument(
        "check_name",
        help="The name of the check to perform under the context",
        default=None,
        nargs="?",
    )

    check_parser.add_argument(
        "--list-parameters",
        "-lp",
        help="print the parameters of the selcted action",
        default=False,
        action="store",
        dest="list_parameters",
    )

    check_parser.add_argument(
        "--parameter",
        "-p",
        help=" set the parameter value with <path> = <value>",
        dest="Set_parameters",
        action="append",
        default=[],
    )

    checklist_parser.add_argument(
        "checkList_name",
        help= "the path to the checkto perfoem under context",
        default = None,
        nargs="?",
    )

    checklist_parser.add_argument(
        "--list-parameters",
        "-lp",
        help="print the parameters of the selcted action",
        default=False,
        action="store",
        dest="list_parameters",
    )

    checklist_parser.add_argument(
        "--parameter",
        "-p",
        help=" set the parameter value with <path> = <value>",
        dest="Set_parameters",
        action="append",
        default=[],
    )

    launcher_parser.add_argument(
        "dcc",
        help="the dcc to start",
        default=None,
        nargs="?"
    )

    launcher_parser.add_argument(
        "--file",
        "-f",
        help=" the file to open within the dcc",
        type=str,
        required=False,
    )
    launcher_parser.add_argument(
        "--check",
        "-c",
        help="the check we want to execute when file open",
        type=str,
        required=False,
    )

    args = vars(parser.parse_args())

    subcommand = args.pop("subcommand", None)
    if subcommand is not None:
        # Execute the appropriate handler according to the subparser
        HANDLERS_MAPPING[subcommand](**args)
    
if __name__ =="__main__":
    main()
