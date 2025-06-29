'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다.
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13
'''
# 일단 하던대로 dfs...
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

graph = [[] for _ in range(N * M)]
for row in range(N):
    for col in range(M):
        if maps[row][col] == 1:
            # 우측
            if col + 1 < M and maps[row][col + 1] == 1:
                graph[row * M + col].append(row * M + (col + 1))
                graph[row * M + (col + 1)].append(row * M + col)
            # 하단
            if row + 1 < N and maps[row + 1][col] == 1:
                graph[row * M + col].append((row + 1) * M + col)
                graph[(row + 1) * M + col].append(row * M + col)

visited = [False] * (N * M)

count = 0
answers = set()

def dfsR(node):
    global count

    if node == N * M - 1:
        answers.add(count + 1)
        return
    
    if visited[node]:
        return

    visited[node] = True
    count += 1
    for neighbor in graph[node]:
        dfsR(neighbor)

    visited[node] = False
    count -= 1
    return
    
dfsR(0)
print(min(answers))
'''
# 7*7에 전부 1로 가득찬 경우조차 못버틴다
# 모든 경로를 탐색할 순 없는데...
# dfs가 아니라 bfs 문제였던 것이다.

from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

# 간선 정보 담긴 그래프 만들기
graph = [[] for _ in range(N * M)]
for row in range(N):
    for col in range(M):
        if maps[row][col] == 1:
            # 우측
            if col + 1 < M and maps[row][col + 1] == 1:
                graph[row * M + col].append(row * M + (col + 1))
                graph[row * M + (col + 1)].append(row * M + col)
            # 하단
            if row + 1 < N and maps[row + 1][col] == 1:
                graph[row * M + col].append((row + 1) * M + col)
                graph[(row + 1) * M + col].append(row * M + col)

def bfs(start):
    visited = [False] * (N * M)
    distance = [0] * (N * M)
    
    queue = deque() # bfs니까 데크 만들고
    queue.append(start) # 큐에 밀어넣고
    visited[start] = True
    distance[start] = 1  # 노드0에 1 저장

    while queue:
        current = queue.popleft() # bottom부터 빼낸다.
        if current == N * M - 1: # 마지막 좌표에 도달하면 종료
            return distance[current] # 현재 노드에 저장된 거리 반환
            
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1 # 거리에 1 더해서 넘김
                queue.append(neighbor) # 큐에 밀어넣기

    return # 도달하지 않은 경우

answer = bfs(0)
print(answer)