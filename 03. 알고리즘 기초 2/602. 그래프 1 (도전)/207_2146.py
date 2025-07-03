'''
문제
여러 섬으로 이루어진 나라가 있다.
이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다.
하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다.
그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고,
그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다.
이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다.
다음은 세 개의 섬으로 이루어진 나라의 지도이다.



위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다.
이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다.
가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다.
다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.



물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나,
위의 경우가 놓는 다리의 길이가 3으로 가장 짧다(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

입력
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다.
그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다.
항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

출력
첫째 줄에 가장 짧은 다리의 길이를 출력한다.

예제 입력 1 
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
'''
# 각 섬들을 데크에 전부 밀어넣고 bfs를 돌려보자.
# bfs가 다음 섬에 닿으면 그 순간 가장 짧은 다리가 생긴다.

# 섬을 이루는 노드끼리 뭉쳐놓은 정보가 담긴 리스트가 따로 필요할 듯.

import sys
sys.setrecursionlimit(10**6)

from collections import deque

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]

# 섬 정보가 담긴 그래프
island_graph = [[] for _ in range(N * N)]
# 전체가 간선으로 이어진 그래프
graph = [[] for _ in range(N * N)]

for row in range(N):
    for col in range(N):
        current = row * N + col

        if col + 1 < N:
            right = row * N + (col + 1)
            graph[current].append(right)
            graph[right].append(current)
            if maps[row][col] == 1 and maps[row][col + 1] == 1:
                island_graph[current].append(right)
                island_graph[right].append(current)
        if row + 1 < N:
            down = (row + 1) * N + col
            graph[current].append(down)
            graph[down].append(current)
            if maps[row][col] == 1 and maps[row + 1][col] == 1:
                island_graph[current].append(down)
                island_graph[down].append(current)

# dfsR로 연결요소 찾아서 섬끼리 노드 묶기
islands = []
visited = [False] * (N * N)
def dfsR(node, group):
    if visited[node]:
        return
    visited[node] = True
    group.add(node)
    for neighbor in island_graph[node]:
        dfsR(neighbor, group)

# 찾은 연결요소들을 저장하기
for i in range(N * N):
    if not visited[i] and maps[i // N][i % N] == 1:
        group = set()
        dfsR(i, group)
        islands.append(group)

# bfs로 다음 섬까지 가는 최단경로 찾기
def bfs(island):
    distance = [-1] * (N * N)
    queue = deque()
    for node in island: # 섬의 노드를 방문 처리
        queue.append(node)
        distance[node] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1: # 방문 안된 노드에 한해서 순회
                if maps[neighbor // N][neighbor % N] == 1:
                    return distance[current]
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

# 각 섬에서 지을 수 있는 가장 짧은 다리를 전부 확인
answer = 9999
for island in islands:
    answer = min(answer, bfs(island))
print(answer)

'''
6
1 0 0 1 1 1
1 0 0 0 0 1
1 0 0 0 0 0
1 0 0 0 0 1
1 1 1 1 1 1
0 0 0 0 0 0
'''