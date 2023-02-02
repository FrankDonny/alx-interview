#!/usr/bin/python3
"""lockboxes module"""


def canUnlockAll(boxes):
    """function to unlock boxes"""
    unlocked_boxes = set([0])
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == len(boxes)
