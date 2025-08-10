'''
문제
N×M의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
이동하지 않고 같은 칸에 머물러있는 경우도 가능하다.
이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다.

이번 문제에서는 낮과 밤이 번갈아가면서 등장한다.
가장 처음에 이동할 때는 낮이고, 한 번 이동할 때마다 낮과 밤이 바뀌게 된다.
이동하지 않고 같은 칸에 머무르는 경우에도 낮과 밤이 바뀌게 된다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.
단, 벽은 낮에만 부술 수 있다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
1 4 1
0010
예제 출력 1 
5
예제 입력 2 
1 4 1
0100
예제 출력 2 
4
예제 입력 3 
6 4 1
0100
1110
1000
0000
0111
0000
예제 출력 3 
15
예제 입력 4 
6 4 2
0100
1110
1000
0000
0111
0000
예제 출력 4 
9
'''

# 14442에서 낮밤조건 추가. 벽은 낮에만 부술 수 있다.
# 스택에만 TF로 구분해서 넣어주면 되지 않을까? 머무르기도 생각해야함.
# day가 0이면 낮이고, 1이면 밤이다.
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start, K):
    # 4차원배열 [time][crashed][x][y] 낮, 밤 분리
    visited = [[[[-1] * M for _ in range(N)] for _ in range(K + 1)] for _ in range(2)]

    queue = deque()
    queue.append([0] + start + [0])
    visited[0][0][start[0]][start[1]] = 1
    
    while queue:
        # 큐에 [crashed, x, y, time] 형태로 저장
        crashed, x, y, time = queue.popleft()

        # x, y가 목적지에 도달하면 종료
        if x == N - 1 and y == M - 1:\
            return visited[0][crashed][x][y] if time == 0 else visited[1][crashed][x][y]
        
        # 상하좌우에 대해 반복
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 인덱스에러 확인
            if 0 <= nx < N and 0 <= ny < M:

                # 낮일 경우
                if time == 0:

                    # 다음 칸이 벽이고, 벽뚫 횟수가 남아있으며, 미방문 상태인 경우
                    if board[nx][ny] == 1 and crashed < K and visited[1][crashed + 1][nx][ny] == -1:
                        queue.append([crashed + 1, nx, ny, 1])
                        visited[1][crashed + 1][nx][ny] = visited[0][crashed][x][y] + 1

                    # 다음 칸이 벽이 아니며, 미방문 상태인 경우
                    elif board[nx][ny] == 0 and visited[1][crashed][nx][ny] == -1:
                        queue.append([crashed, nx, ny, 1])
                        visited[1][crashed][nx][ny] = visited[0][crashed][x][y] + 1

                # 밤일 경우
                elif time == 1:

                    # 다음 칸이 벽이고, 벽뚫 횟수가 남아있으며, 미방문 상태지만 낮이 되길 기다려야 하는 경우
                    if board[nx][ny] == 1 and crashed < K and visited[0][crashed + 1][nx][ny] == -1:
                        queue.append([crashed, x, y, 0])
                        visited[0][crashed][x][y] = visited[1][crashed][x][y] + 1

                    # 다음 칸이 벽이 아니며, 미방문 상태인 경우
                    elif board[nx][ny] == 0 and visited[0][crashed][nx][ny] == -1:
                        queue.append([crashed, nx, ny, 0])
                        visited[0][crashed][nx][ny] = visited[1][crashed][x][y] + 1

    # 큐 소진
    return -1

# 시작 좌표, 부술수 있는 벽의 개수 집어넣기
print(bfs([0, 0], K))
'''

# 너무 쓸데없는 경로를 많이 탐색하는 것 같다.
# 그리고 굳이 4차원배열까지 가야 할까?

import sys
input = sys.stdin.readline

from collections import deque

N, M, K = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(start):

    # [x][y] 에 벽을 부순 횟수를 저장, 초기값은 벽 부술 수 있는 총 횟수보다 1 크게 설정
    visited = [[K + 1 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append(start)
    visited[0][0] = 0

    current_distance = 1
    time = True

    while queue:
        # 같은 distance를 가지는 노드를 전부 순회하는 느낌.
        for _ in range(len(queue)):
            x, y, crashed = queue.popleft()

            # 좌표 도달로 조건 만족 시 종료
            if x == N - 1 and y == M - 1:
                print(current_distance)
                return

            # 상하좌우 4방향에 대해 반복 확인
            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                # 인덱스 체크 하고, 이전 시행보다 벽을 덜 부수고 도착했을 때만 실행
                if 0 <= nx < N and 0 <= ny < M and crashed < visited[nx][ny]:

                    # 다음 칸이 벽이 아닌 경우
                    if board[nx][ny] == "0":
                        queue.append((nx, ny, crashed))
                        visited[nx][ny] = crashed

                    # 다음 칸이 벽이며, 벽을 부술 수 있는 횟수가 남아있는 경우
                    elif crashed < K:

                        # 밤인 경우 제자리에서 하루를 기다린다.
                        if not time:
                            queue.append((x, y, crashed))

                        # 낮인 경우 벽을 부순다.
                        else:
                            queue.append((nx, ny, crashed + 1))
                            visited[nx][ny] = crashed # + 1을 해도 되고, 안해도 되고??

        # 다음 시행으로 넘어가기 전에 이동횟수 +1, 낮밤 바꾸기를 해준다.
        current_distance += 1
        time = not time

    # 큐 소진 시 조건 만족 불가능
    print(-1)
    return

bfs((0, 0, 0))

# 아, 쓸데없이 생각할 필요가 없었다는 거야.
# 결국 모든 건 아이디어. 틀에 박히면 안 된다는 거지...