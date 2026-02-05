# Authored by : marigold2003
# Date : 2026-02-05
# Link : https://www.acmicpc.net/problem/17070

import sys

input = sys.stdin.readline


# [Summary]

# 좌상단에서 파이프를 이동시켜서 우하단으로 옮겨야 한다.

# 가로상태에서는 우, 우하로 이동 가능
# 대각상태에서는 우, 우하, 하로 이동 가능
# 세로상태에서는 우하, 하로 이동 가능

# 대각상태는 4칸을 전부 차지하고 있다.
# 이동해서 차지할 칸이 벽이라면 이동할 수 없다.

# 이동시킬 수 있는 모든 경우의 수를 구하시오.


def DynamicP() -> None:

    # [Ideas]

    # dfsR은 시간초과가 난다.
    # 같은 칸에 도착할 때 중복된 연산이 반복되니까.
    # 이걸 없애려면 dp가 답이다.

    ##########

    N = int(input())

    # 보드는 우측과 하단에 padding해서 저장한다.
    board = list(list(map(int, input().split())) + [1] for _ in range(N))
    board.append([1] * (N + 1))

    # [상태][행][열] 가로0 세로1 대각2
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(3)]

    # 가로0, 0, 1로 시작
    dp[0][0][1] = 1

    # padding을 해뒀기 때문에 인덱스 초과 처리는 필요 없다.

    # 첫 행부터 시작하여 좌측 열부터 이동시켜 나간다.
    # 현재 칸에 있는 값은 현재 칸에 도달하는 경로의 수가 된다.
    for r in range(N):
        for c in range(N):
            # 가로로 이동하는 경우 현재 칸에 가로, 대각 상태로 있어야 한다.
            if not board[r][c + 1]:
                dp[0][r][c + 1] += dp[0][r][c] + dp[2][r][c]

            # 세로로 이동하는 경우 현재 칸에 세로, 대각 상태로 있어야 한다.
            if not board[r + 1][c]:
                dp[1][r + 1][c] += dp[1][r][c] + dp[2][r][c]

            # 대각으로 이동하는 경우 현재 칸에 있는 모든 상태를 더한다.
            if not (board[r + 1][c] or board[r][c + 1] or board[r + 1][c + 1]):
                dp[2][r + 1][c + 1] += dp[0][r][c] + dp[1][r][c] + dp[2][r][c]

    # N-1, N-1에 도착한 각 상태들을 더하면 된다.
    print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])

    ##########

    return


def BruteForce() -> None:

    # [Ideas]

    # 모든 경우를 시뮬레이션 할 수 있지 않을까?
    # 구현만 잘 하면 될 것 같은데.

    # dp도 사용 가능할 것 같다.

    # 시뮬레이션은 재귀 dfs를 사용해볼 수 있을 듯.
    # 보드는 전역으로 두고, 상태와 좌표를 저장해서 돌리자.

    ##########

    N = int(input())

    # 보드는 우측과 하단에 padding해서 저장한다.
    board = list(list(map(int, input().split())) + [1] for _ in range(N))
    board.append([1] * (N + 1))

    answer = 0

    # 상태와 도달좌표(다음 이동 시작좌표)
    # 가로1 대각2 세로3 으로 한다.
    def dfsR(condition, r, c):
        nonlocal answer

        if r == N - 1 and c == N - 1:
            answer += 1
            return

        # padding 된 보드이므로 0 <= x < N같은 인덱스처리가 필요 없다.

        # 가로 대각에서는 가로이동 가능
        if condition == 1 or condition == 2:
            if not board[r][c + 1]:
                dfsR(1, r, c + 1)

        # 세로 대각에서는 세로이동 가능
        if condition == 2 or condition == 3:
            if not board[r + 1][c]:
                dfsR(3, r + 1, c)

        # 세 곳 중 하나라도 벽이 있지 않는다면 모든 경우에서 대각이동 가능.
        if not (board[r][c + 1] or board[r + 1][c] or board[r + 1][c + 1]):
            dfsR(2, r + 1, c + 1)

    dfsR(1, 0, 1)
    print(answer)

    ##########

    return


# [Review]

# padding에 대하여 배웠다.
# 그리고 dp의 세계는 넓고도 깊다는 것을... 이건 아주 얕은 편이지만.

if __name__ == "__main__":
    # BruteForce()
    DynamicP()
