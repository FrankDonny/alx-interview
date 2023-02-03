#!/usr/bin/python3
"""lockboxes module"""


# def canUnlockAll(boxes):
#     """function to unlock boxes"""
#     unlocked_boxes = set([0])
#     queue = [0]

#     while queue:
#         box = queue.pop(0)
#         for key in boxes[box]:
#             if key not in unlocked_boxes:
#                 unlocked_boxes.add(key)
#                 queue.append(key)

#     return len(unlocked_boxes) == len(boxes)


# boxes = list of list
# box is in sequential order from 0 to n-1
# n = number of locked boxes
# a key with the same number as a box opens that box
def canUnlockAll(boxes):
    """function to unlock boxes"""
    boxes.sort()
    count = 0
    for i in range(1, len(boxes)):
        # print(f"i->{i}")
        for key in boxes[i]:
            # print(f"key->{key}, box[{i}]->{boxes[i]}")
            if key == i:
                count += 1
                # print(f"count->{count}")
    if count == len(boxes) - 1:
        return True
    return False


# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))
# boxes = [[1], [2], [3], [4], []]
# boxes.sort()
# print(boxes)
# second = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# second.sort()
# print(second)
# another = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# another.sort()
# print(another)
