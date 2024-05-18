from pythonclient.check_buffer import CheckBuffer
from pythonclient.check_query import CheckQuery
from pythonclient.checkRepository.test_check import TestCheck


if __name__ == "__main__":
    check_buffer = CheckBuffer()
    test = TestCheck("test_check", check_bufferc)
    print(test)