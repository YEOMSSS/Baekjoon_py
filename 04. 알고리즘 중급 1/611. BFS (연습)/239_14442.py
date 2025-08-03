'''
문제
N×M의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4 1
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
6 4 2
0100
1110
1000
0000
0111
0000
예제 출력 2 
9
예제 입력 3 
4 4 3
0111
1111
1111
1110
예제 출력 3 
-1
'''

# bfs돌리면서 벽을 만날때 한번 뚫게 하고, 그걸 저장해서 다음시행에는 못 뚫게 하자.
# 리스트를 두칸으로 만들어서 뚫었을때 안뚫었을때를 따로 저장해주자.
# 2206
'''
import sys
input = sys.stdin.readline

from collections import deque

N, M, K = map(int, input().split())

maps = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우 dxdy용 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():

    # 0번에 저장되면 벽뚫기 가능한 상태, 1번에 저장되면 더이상 벽 못뚫음
    visited = [[-1] * (K + 1) for _ in range(N * M)]

    # 첫칸도 한칸으로 치니까 1 저장
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        # 현재 coord와 벽뚫여부 가져오기
        current, crashed = queue.popleft()

        # 마지막 coord N*M-1 도착시 조건만족. 벽뚫여부에 따라 visited를 반환

        if current == N * M - 1:
            return visited[-1][crashed]

        # current의 상하좌우마다 반복
        for dx, dy in directions:
            row = current // M + dx
            col = current % M + dy
            next_coord = row * M + col
            
            # 인덱스 확인
            if 0 <= row < N and 0 <= col < M:

                # 벽을 더 뚫을 수 있는 경우
                if crashed != K:

                    # 다음칸이 미방문이며 벽이 아니어서 뚫을 필요가 없는 경우
                    if maps[row][col] == 0 and visited[next_coord][crashed] == -1:
                        visited[next_coord][crashed] = visited[current][crashed] + 1
                        queue.append((next_coord, crashed))

                    # 다음칸이 미방문이며 벽이고 벽을 뚫어도 벽뚫 횟수가 남은 경우
                    elif maps[row][col] == 1 and visited[next_coord][crashed] == -1 and crashed != K - 1:
                        visited[next_coord][crashed + 1] = visited[current][crashed] + 1
                        queue.append((next_coord, crashed + 1))

                    # 다음칸이 미방문이며 벽이고 마지막으로 뚫을 수 있는 벽인 경우
                    elif maps[row][col] == 1 and visited[next_coord][crashed] == -1 and crashed == K - 1:
                        visited[next_coord][crashed + 1] = visited[current][crashed] + 1
                        queue.append((next_coord, crashed + 1))

                # 다음칸이 미방문이며 벽이 아니고 벽 뚫기를 더 사용할 수 없는 경우
                elif maps[row][col] == 0 and visited[next_coord][crashed] == -1 and crashed == K:
                    visited[next_coord][crashed] = visited[current][crashed] + 1
                    queue.append((next_coord, crashed))

    # 모든 경우의 수에서 N*M-1에 도착하지 못하면 -1 반환
    return -1

print(bfs())
'''
# 은근히 빡세네?
# 시간초과가 난다.

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start, K):
    # 3차원배열 [crashed][x][y]
    visited = [[[-1] * M for _ in range(N)] for _ in range(K + 1)]

    queue = deque()
    queue.append([0] + start)
    visited[0][start[0]][start[1]] = 0
    
    while queue:
        # 큐에 [crashed, x, y] 형태로 저장
        crashed, x, y = queue.popleft()

        # x, y가 목적지에 도달하면 종료
        if x == N - 1 and y == M - 1:
            return visited[crashed][x][y] + 1
        
        # 상하좌우에 대해 반복
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 인덱스에러 확인
            if 0 <= nx < N and 0 <= ny < M:

                # 다음 칸이 벽이고, 벽뚫 횟수가 남아있으며, 미방문 상태인 경우
                if board[nx][ny] == 1 and crashed < K and visited[crashed + 1][nx][ny] == -1:
                    queue.append([crashed + 1, nx, ny])
                    visited[crashed + 1][nx][ny] = visited[crashed][x][y] + 1

                # 다음 칸이 벽이 아니며, 미방문 상태인 경우
                elif board[nx][ny] == 0 and visited[crashed][nx][ny] == -1:
                    queue.append([crashed, nx, ny])
                    visited[crashed][nx][ny] = visited[crashed][x][y] + 1
    # 큐 소진
    return -1

# 시작 좌표, 부술수 있는 벽의 개수 집어넣기
print(bfs([0, 0], K))

# 이놈의 시간초과, pypy로만 풀린다.