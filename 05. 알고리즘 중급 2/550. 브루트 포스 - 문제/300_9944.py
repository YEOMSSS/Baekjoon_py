# Authored by : marigold2003
# Date : 2026-02-03
# Link : https://www.acmicpc.net/problem/9944

import sys

input = sys.stdin.readline


# [Summary]

# N*M 보드에 벽이 있다.
# 이동은 상하좌우로 할 수 있고, 벽을 만나거나 이동한 칸을 만나면 멈춘다.
# 모든 칸을 방문하기 위한 이동 횟수의 최솟값을 구하여라.


def main() -> None:

    # [Ideas]

    # 그래프라고 생각했는데, 그러면 오히려 복잡해질 것 같다.

    # 경로가 생기는 가짓수는 1M개를 넘지 않는다.
    # 재귀 백트래킹으로 가지치키를 잘 해보자.
    # 지나온 칸의 정보를 계속 내려보내면 되지 않을까?

    ##########

    sys.setrecursionlimit(10**6)

    i = 0
    while True:
        i += 1
        testcase = input().rstrip()
        if not testcase:
            return

        N, M = map(int, testcase.split())
        board = tuple(tuple(input().rstrip()) for _ in range(N))
        visited = [[False for _ in range(M)] for _ in range(N)]

        walls = 0
        for r in range(N):
            for c in range(M):
                if board[r][c] == "*":
                    visited[r][c] = True
                    walls += 1

        # 칸이 하나면 경로는 무조건 1개
        if walls + 1 == N * M:
            print(f"Case {i}: 0")
            continue

        answer = sys.maxsize

        # 상하좌우로 이동 후 백트래킹
        def backtrack(r, c, visited: list, moves, rest):
            nonlocal answer

            # 최솟값 이상 이동하는 경로는 필요 없음
            if moves >= answer:
                return

            # 모든 경로를 지나는 것에 성공했을 때
            if rest == 0:
                answer = min(answer, moves)
                return

            # 상하좌우에 대해 각각 재귀
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):

                nr, nc = r + dr, c + dc
                count = 0

                while 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    count += 1
                    visited[nr][nc] = True
                    nr, nc = nr + dr, nc + dc

                if count > 0:
                    backtrack(nr - dr, nc - dc, visited, moves + 1, rest - count)

                    # 복구
                    nr, nc = r, c
                    for _ in range(count):
                        nr, nc = nr + dr, nc + dc
                        visited[nr][nc] = False

        for r in range(N):
            for c in range(M):
                # 벽에서는 시작할 수 없다.
                if visited[r][c]:
                    continue

                visited[r][c] = True
                backtrack(r, c, visited, 0, N * M - walls - 1)
                visited[r][c] = False

        print(f"Case {i}: {answer if not answer == sys.maxsize else -1}")

    ##########

    return


# [Review]

# 가지를 쳐 보자.
# 백트래킹 연습에 도움이 많이 될 법한 문제.
# 아악! 재귀문제는 pypy로 풀지 말지어다

if __name__ == "__main__":
    main()
