def canUnlockAll(boxes):
    unlocked_boxes = set([0])
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == len(boxes)


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
