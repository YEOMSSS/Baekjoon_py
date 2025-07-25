'''
문제
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다.
데스 나이트가 있는 곳이 (r, c)라면,
(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다.
데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자.
체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다.
둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다.
이동할 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
7
6 6 0 1
예제 출력 1 
4
예제 입력 2 
6
5 1 0 5
예제 출력 2 
-1
예제 입력 3 
7
0 3 4 3
예제 출력 3 
2
'''

# 체스보드를 만들어놓고, bfs내에서 6가지 종류의 이동경로를 큐에 밀어넣는다.

from collections import deque

N = int(input())
R1, C1, R2, C2 = map(int, input().split())

# 보드판 만들어놓기 (1차원 배열)
board = [] * (N * N)

# 이동 가능 칸들의 변화량을 저장해둔 리스트
moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

# 이동횟수와 이동여부를 파악
visited = [-1] * (N * N)

def bfs():
    queue = deque()
    queue.append((R1, C1))
    visited[R1 * N + C1] = 0

    while queue:
        row, col = queue.popleft()
        if row == R2 and col == C2:
            return

        # 큐에 (dR, dC) 형태로 push
        # 보드판을 넘기는 경우는 제외, 방문되었어도 제외
        for dR, dC in moves:
            nR = row + dR
            nC = col + dC
            if 0 <= nR < N and 0 <= nC < N and visited[nR * N + nC] == -1:
                    queue.append((nR, nC))
                    visited[nR * N + nC] = visited[row * N + col] + 1

bfs()
print(visited[R2 * N + C2])

# 깔끔하게!