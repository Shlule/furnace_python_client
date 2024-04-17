from enum import IntEnum

class CheckStatus(IntEnum):

    COMPLETED = 0
    INITIALIZED = 1
    UNCHECK = 2
    WAITING_FOR_FIX = 3
    PROCESSING = 4
    INVALID = 5
    ERROR = 6
        