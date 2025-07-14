'''
from collections import deque

N, K = map(int, input().split())

num_list = list(range(1, N + 1))

queue = deque(num_list)
print("<", end= "")
while len(queue) != 1:
    queue.rotate(-(K - 1))
    target_to_pop = queue.popleft()
    print(target_to_pop, end= ", ")    

print(*queue, end= "")
print(">")
'''

from collections import deque

N, K = map(int, input().split())

num_list = list(range(1, N + 1))

queue = deque(num_list)
result = []

while len(queue):
    queue.rotate(-(K - 1))
    target_to_pop = queue.popleft()
    result.append(target_to_pop)


print(f"<{', '.join(map(str, result))}>")