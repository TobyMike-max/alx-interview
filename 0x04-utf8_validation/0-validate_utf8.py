#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Validates utf-8 in Parameter data

    Args:
        List(Int): A list of numbers
    Return:
        True if the data validates utf-8
        Otherwise False

    Example:
        For this data to be utf-8 compliant it must follow a certain pattern
        Every single byte(8 bit) integer must start with 0, while,
        Every multi byte(4 bytes most) would start with either of these headers:
        * 110 for 2 bytes
        * 1110 for 3 bytes
        * 11110 for 4 bytes
        Followed closely by 10 as header for the remaining bytes
        If a data doesn't comply with these pattern it isn't utf-8 compliant
        
        data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
        N.B Each integer reps 1 byte of data, therefore handle the 8 least
        significant bits of each integer.
        This data above is utf-8 compliant because all numbers are single byte,
        therefore all start with 0 to complete their 8bits and there are no encoded
        bytes in the preceeding integer.
        
        count variable just checks the number of encoded bytes in the
        preceeding integers for a character
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
