import sys
from collections import deque

data = sys.stdin.read().splitlines()
left = deque(data[0])
right = deque()

for line in data[2:]:  # data[1]은 명령 개수, 나머지는 명령어
    if line == "L":
        if left:
            right.appendleft(left.pop())
    elif line == "D":
        if right:
            left.append(right.popleft())
    elif line == "B":
        if left:
            left.pop()
    else:
        # P x 형태
        _, char = line.split()
        left.append(char)

print(''.join(left + right))
