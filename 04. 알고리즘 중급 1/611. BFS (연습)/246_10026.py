'''
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1)
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1 
4 3
'''

# bfs 골드5는 이제 가볍게

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

board = [input().rstrip() for _ in range(N)]

# 상하좌우
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs_common(row, col, color):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True

    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            # 인덱스, 방문, 색상 확인
            if ny < 0 or N <= ny or nx < 0 or N <= nx:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] != color:
                continue

            queue.append((ny, nx))
            visited[ny][nx] = True

def bfs_uncommon(row, col, color):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True

    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            # 인덱스, 방문, 색상 확인
            if ny < 0 or N <= ny or nx < 0 or N <= nx:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] != color:
                # 적록색맹일 땐 R == G
                if color == "B" or board[ny][nx] == "B":
                    continue

            queue.append((ny, nx))
            visited[ny][nx] = True

visited = [[False for _ in range(N)] for _ in range(N)]

result_common = 0
for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        bfs_common(y, x, board[y][x])
        result_common += 1

visited = [[False for _ in range(N)] for _ in range(N)]

result_uncommon = 0
for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        bfs_uncommon(y, x, board[y][x])
        result_uncommon += 1

print(result_common, result_uncommon)
