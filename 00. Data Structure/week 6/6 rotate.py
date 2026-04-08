from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.rotate(1)
print(dq)
dq.rotate(-2)
print(dq)
