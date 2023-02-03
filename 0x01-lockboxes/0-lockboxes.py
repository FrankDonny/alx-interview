#!/usr/bin/python3
"""lockboxes module"""


def canUnlockAll(boxes):
    """function to unlock boxes"""
    boxes.sort()
    count = 0
    for i in range(1, len(boxes)):
        for key in boxes[i]:
            if key == i:
                count += 1
    if count == len(boxes) - 1:
        return True
    return False
