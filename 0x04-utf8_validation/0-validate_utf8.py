#!/usr/bin/python3
"""module for utf-8"""


def validUTF8(data):
    """the function"""
    num_bytes = 0

    for i in data:
        # Check if the current byte is a continuation byte
        if num_bytes > 0 and (i >> 6) == 0b10:
            num_bytes -= 1
        # Check if the current byte is the start of a multi-byte sequence
        elif num_bytes == 0:
            if (i >> 7) == 0:
                # One-byte character
                continue
            elif (i >> 5) == 0b110:
                # Two-byte character
                num_bytes = 1
            elif (i >> 4) == 0b1110:
                # Three-byte character
                num_bytes = 2
            elif (i >> 3) == 0b11110:
                # Four-byte character
                num_bytes = 3
            else:
                # Invalid multi-byte sequence
                return False
        else:
            # Invalid continuation byte
            return False

    # Check if there are any remaining bytes in a multi-byte sequence
    return num_bytes == 0
