'''
문제
N×M의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1
'''

# bfs돌리면서 벽을 만날때 한번 뚫게 하고, 그걸 저장해서 다음시행에는 못 뚫게 하자.
# 리스트를 두칸으로 만들어서 뚫었을때 안뚫었을때를 따로 저장해주자.

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

maps = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우 dxdy용 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    # 0번에 저장되면 벽 안뚫은상태, 1번에 저장되면 벽 뚫은상태
    visited = [[-1] * 2 for _ in range(N * M)]

    # 첫칸도 한칸으로 치니까 1 저장
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        # 현재 coord와 벽뚫여부 가져오기
        current, crashed = queue.popleft()

        # 마지막 coord N*M-1 도착시 조건만족. 벽뚫여부에 따라 visited를 반환
        if current == N * M - 1:
            return visited[-1][0] if crashed == 0 else visited[-1][1]

        # current의 상하좌우마다 반복
        for dx, dy in directions:
            row = current // M + dx
            col = current % M + dy
            next_current = row * M + col
            
            # 인덱스 확인
            if 0 <= row < N and 0 <= col < M:
                # 벽을 아직 뚫지 않은 경우
                if crashed == 0:
                    # 다음칸이 미방문이며 벽이 아니어서 뚫을 필요가 없는 경우
                    if maps[row][col] == 0 and visited[next_current][0] == -1:
                        visited[next_current][0] = visited[current][0] + 1
                        queue.append((next_current, 0))
                        
                    # 다음칸이 미방문이며 벽이어서 뚫어야 하는 경우
                    elif maps[row][col] == 1 and visited[next_current][1] == -1:
                        visited[next_current][1] = visited[current][0] + 1
                        queue.append((next_current, 1))

                # 벽 뚫기를 사용했고, 다음칸이 미방문이며 벽이 아닌 경우
                elif crashed == 1 and maps[row][col] == 0 and visited[next_current][1] == -1:
                    visited[next_current][1] = visited[current][1] + 1
                    queue.append((next_current, 1))

    # 모든 경우의 수에서 N*M-1에 도착하지 못하면 -1 반환
    return -1

print(bfs())

# 아~ 혼자힘으로 원콤이에용.