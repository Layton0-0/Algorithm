from collections import deque

queue = deque()

queue.append(3)  # [3]
queue.append(5)  # [3, 5]
queue.append(2)  # [3, 5, 2]
queue.popleft()  # [5, 2]
queue.append(8)  # [5, 2, 8]
queue.popleft()  # [2, 8]
