# Authored by : marigold2003
# Date : 2026-01-31
# Link : https://www.acmicpc.net/problem/2210

import sys

input = sys.stdin.readline


# [Summary]

# 5*5 보드의 아무데서나 시작해가지고 상하좌우로 이동할 수 있다.
# 5회 이동해서 6자리 수를 만드는 경우의 수는?


def main():

    # [Ideas]

    # 이건 그래프를 사용해야 할 것 같다.
    # dfsR로 브루트포스 완전탐색 하면 될 듯?

    ##########

    board = [list(input().split()) for _ in range(5)]

    result = set()

    def dfsR(r, c, n, curr):
        if n == 6:
            result.add(curr)
            return

        for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue
            dfsR(nr, nc, n + 1, curr + board[nr][nc])

    for r in range(5):
        for c in range(5):
            dfsR(r, c, 1, board[r][c])

    print(len(result))

    ##########

    return


# [Review]

# 아이디어만 떠올리면 구현은 어렵지 않은 문제.

if __name__ == "__main__":
    main()
