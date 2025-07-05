'''
문제
알고스팟 운영진이 모두 미로에 갇혔다.
미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다.
미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다.
즉, 여러 명이 다른 방에 있을 수는 없다.
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다.
즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다.
벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만,
안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다.
다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다.
0은 빈 방을 의미하고, 1은 벽을 의미한다.

(1, 1)과 (N, M)은 항상 뚫려있다.

출력
첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.

예제 입력 1 
3 3
011
111
110
예제 출력 1 
3
예제 입력 2 
4 2
0001
1000
예제 출력 2 
0
예제 입력 3 
6 6
001111
010000
001111
110001
011010
100010
예제 출력 3 
2
'''
# 뭔가 그 섬문제랑 비슷한거같은데. 다리놓는거.
# 다르긴하네. 흠.. 간선을 이을 수 있나?

# 도착지가 0이면 가중치0이고
# 도착지가 1이면 가중치1.

# 깔끔하게 풀었는데?

# 뭔가 그 섬문제랑 비슷한거같은데. 다리놓는거.
# 다르긴하네. 흠.. 간선을 이을 수 있나?

# 도착지가 0이면 가중치0이고
# 도착지가 1이면 가중치1.

import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

# 상하좌우가 이어진 간선
graph = [[] for _ in range(M * N)]
for row in range(N):
    for col in range(M):
        current = row * M + col
        if col + 1 < M:
            left = current + 1
            graph[current].append(left)
            graph[left].append(current)
        if row + 1 < N:
            down = current + M
            graph[current].append(down)
            graph[down].append(current)

queue = deque()
distance = [-1] * (M * N)

queue.append(0)
distance[0] = 0

while queue:
    current = queue.popleft()
    if current == N * M:
        break
    
    for neighbor in graph[current]:
        # 더 빨라질 일은 없어서 갱신은 따로 필요 없다.
        # if distance[neighbor] == -1 or distance[neighbor] > distance[current]:
        if distance[neighbor] == -1:
            # 도착지가 0이면 가중치 0. appendleft로 우선순위에 두기
            if maps[neighbor // M][neighbor % M] == 0:
                distance[neighbor] = distance[current]
                queue.appendleft(neighbor)
            # 도착지가 1이면 가중치 1.
            elif maps[neighbor // M][neighbor % M] == 1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

print(distance[-1])