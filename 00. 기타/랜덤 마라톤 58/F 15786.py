from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
hint_origin = list(input().rstrip())

for _ in range(N):
    target = list(input().rstrip())
    queue = deque(target)
    hint = deque(hint_origin) # 반복마다 힌트 복사
    while queue and hint:
        current = queue.popleft()
        if hint[0] == current:
            hint.popleft()

    if not hint:
        print("true")
    else:
        print("false")  