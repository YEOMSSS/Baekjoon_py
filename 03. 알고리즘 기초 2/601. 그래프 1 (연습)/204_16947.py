
'''
문제
서울 지하철 2호선은 다음과 같이 생겼다.



지하철 2호선에는 51개의 역이 있고, 역과 역 사이를 연결하는 구간이 51개 있다.
즉, 정점이 51개이고, 양방향 간선이 51개인 그래프로 나타낼 수 있다.
2호선은 순환선 1개와 2개의 지선으로 이루어져 있다.
한 역에서 출발해서 계속 가면 다시 출발한 역으로 돌아올 수 있는 노선을 순환선이라고 한다.
지선은 순환선에 속하는 한 역에서 시작하는 트리 형태의 노선이다.

두 역(정점) 사이의 거리는 지나야 하는 구간(간선)의 개수이다.
역 A와 순환선 사이의 거리는 A와 순환선에 속하는 역 사이의 거리 중 최솟값이다.

지하철 2호선과 같은 형태의 노선도가 주어졌을 때, 각 역과 순환선 사이의 거리를 구해보자.

입력
첫째 줄에 역의 개수 N(3 ≤ N ≤ 3,000)이 주어진다.
둘째 줄부터 N개의 줄에는 역과 역을 연결하는 구간의 정보가 주어진다.
같은 구간이 여러 번 주어지는 경우는 없고, 역은 1번부터 N번까지 번호가 매겨져 있다.
임의의 두 역 사이에 경로가 항상 존재하는 노선만 입력으로 주어진다.

출력
총 N개의 정수를 출력한다.
1번 역과 순환선 사이의 거리, 2번 역과 순환선 사이의 거리, ...,
N번 역과 순환선 사이의 거리를 공백으로 구분해 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 네가 재귀호출을 한다면 제발 기억해!!

from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

path = []
cycle_nodes = []

def dfsR(current, parent):
    global cycle_nodes

    visited[current] = True
    path.append(current)

    for neighbor in graph[current]:
        # 방문하지 않은 노드에 대해 dfsR
        if not visited[neighbor]:
            if dfsR(neighbor, current): # 사이클 발견되면 그대로 재귀 종료
                return True
        # 방문된 노드인데 부모노드가 아니라면 사이클. 부모노드면 그냥 양방향
        elif neighbor != parent:
            start_index = path.index(neighbor)
            cycle_nodes = path[start_index:] # 사이클이 시작된 부분부터 슬라이싱
            return True
    path.pop() # 루프가 끝나면 현재 경로에서 삭제

dfsR(1, -1) # cycle_nodes가 만들어짐.

# bfs를 돌려서 사이클까지의 최단거리를 전부 저장한다.

distance = [-1] * (N + 1) # distance가 -1이면 방문하지 않은 노드
queue = deque()
# 사이클을 구성하는 노드를 전부 큐에 밀어넣고 방문 처리
for node in cycle_nodes:
    queue.append(node)
    distance[node] = 0

while queue:
    # 사이클을 구성하는 노드부터 popleft됨.
    current = queue.popleft()

    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

print(" ".join(map(str, distance[1:])))
