'''
문제
체스판 위에 한 나이트가 놓여져 있다.
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다.
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다.
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
체스판의 크기는 l × l이다.
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
'''
# 드디어 나이트 문제를 푸는구나.
# 간선으로 나이트가 이동가능한 8칸을 이어서 그래프를 만들어 보자.

import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

knight_moves = [
    (1, -2), (2, -1), # 좌하
    (1, 2), (2, 1) # 우하
]

for _ in range(T):

    L = int(input())
    curX, curY = map(int, input().split())
    desX, desY = map(int, input().split())
    if curX == desX and curY == desY:
        print(0)
        continue

    graph = [[] for _ in range(L * L)]
    for row in range(L):
        for col in range(L):
            index = row * L + col
            for dx, dy in knight_moves:
                nx, ny = row + dx, col + dy
                if 0 <= nx < L and 0 <= ny < L:
                    neighbor = nx * L + ny
                    graph[index].append(neighbor)
                    graph[neighbor].append(index)

    def bfs(start):
        visited = [False] * (L * L)
        distance = [0] * (L * L)

        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    if neighbor == desX * L + desY:
                        return distance[current] + 1 # 다음 이동으로 도착 가능하면 반환
                    visited[neighbor] = True
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)
    
    print(bfs(curX * L + curY))

# 그래프를 만들지 않고 bfs만 이용해서도 풀 수 있을 것 같다.
# while이 돌 때마다 8방향을 확인해주는 식으로도 풀이 가능할 듯.