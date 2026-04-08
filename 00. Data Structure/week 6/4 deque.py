from collections import deque

myQueue = deque([10, 20, 30])

myQueue.append(40)
myQueue.appendleft(50)

myQueue.pop()
myQueue.popleft()

print(myQueue)
