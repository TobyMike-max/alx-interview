#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Validates utf-8 in Parameter data

    Args:
        List(Int): A list of numbers
    Return:
        True if the data validates utf-8
        Otherwise False
    """

    count = 0

    for i in data:
        binary = bin(i).replace('0b', '').rjust(8, '0')[-8:]
        if count == 0:
            if binary.startswith('110'):
                count = 1
            elif binary.startswith('1110'):
                count = 2
            elif binary.startswith('11110'):
                count = 3
            elif binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            count -= 1

    if count != 0:
        return False

    return True
