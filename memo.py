from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(101)]

# 사다리와 뱀의 경우, 앞 6칸에 간선을 추가한다.
# 사다리나 뱀이 시작되는 칸에는 간선을 추가하지 않는다.
for _ in range(N + M):
    X, Y = map(int, input().split())
    graph[X] = [0] # 사다리나 뱀이 시작되는 칸을 구분한다.
    for i in range(1, 7):
        if 0 < X - i and graph[X - i] != [0]:
            graph[X - i].append(Y)

# 주사위 범위에 사다리나 뱀이 없는 경우는 6만 넣고,
# 있다면 주사위에 뱀보다 큰 칸을 하나 추가해준다. (100에 도착하는 경우 제외)
# 뱀이 +6이면 하나 작은 칸을 추가해준다.
for i in range(1, 101):
    if graph[i] == [0]:
        continue
    elif graph[i]:
        for j in range(6, 0, -1):
            if i + j < 101:
                if graph[i + j] != [0]:
                    graph[i].append(i + j)
                    break
    else:
        for j in range(6, 0, -1):
            if i + j < 101:
                graph[i].append(i + j)
                break

# 주사위 횟수를 저장함과 동시에 중복 방문이 없도록 한다.
distance = [-1] * 101

# bfs를 돌려 최단거리를 찾는다.
def bfs():
    queue = deque()
    queue.append(1)
    distance[1] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                if neighbor == 100:
                    return

bfs()
print(distance[100])

print(graph)
print(distance)