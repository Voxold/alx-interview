def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = set(boxes[0])  # Start with the keys in the first box

    while keys:
        key = keys.pop()
        if key not in opened and key < n:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))