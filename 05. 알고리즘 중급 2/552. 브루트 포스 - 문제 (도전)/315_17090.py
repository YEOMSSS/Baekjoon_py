# Authored by : marigold2003
# Date : 2026-02-19
# Link : https://www.acmicpc.net/problem/17090


import sys

input = sys.stdin.readline


# [Summary] 미로 탈출하기

# N*M board가 있다.
# 각 칸에는 URDL중 하나가 쓰여 있으며, 상우하좌를 의미한다.
# 각 칸에서 출발할 때, board 밖으로 이동할 수 있으면 탈출 가능한 칸이라 한다.
# board에 있는 탈출 가능한 칸의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 최대 500*500칸이다.
    # 250000회 bfs는 좀 빡세보임.

    # 테두리 칸만 거꾸로 타고올라가면서 검사하면 되지않을까?
    # 어차피 경계를 거쳐야 나갈 수 있다.

    # graph도 쉽게 만들어진다.
    # 각 칸에서 이동 가능한 칸이 하나뿐이니까.
    # 뒤집은 graph는 모든 칸이 하나의 부모를 가진다. tree네.

    # 0행U 0열L N-1행D M-1열R
    # 만족하는 테두리칸을 root로 하는 subtree를 순회하면 되겠다.
    # dfs bfs는 뭐 알아서 하고. 구현도 별로 안어렵겠는데?

    # subtree끼리는 겹칠 일이 없다. 아 쾌적해
    # visited가 필요 없다는 거구만!!

    ##########

    N, M = map(int, input().split())
    board = tuple(tuple(input().rstrip()) for _ in range(N))

    # [row][col][neighbors]
    graph = [[[] for _ in range(M)] for _ in range(N)]
    roots = []

    for r in range(N):
        for c in range(M):
            command = board[r][c]

            # 탈출 가능한 테두리좌표는 root에 append
            if (
                (r == 0 and command == "U")
                or (r == N - 1 and command == "D")
                or (c == 0 and command == "L")
                or (c == M - 1 and command == "R")
            ):
                roots.append((r, c))
                continue

            # 도착칸 -> 시작칸으로 digraph 만들기
            match command:
                case "U":
                    graph[r - 1][c].append((r, c))
                case "D":
                    graph[r + 1][c].append((r, c))
                case "L":
                    graph[r][c - 1].append((r, c))
                case "R":
                    graph[r][c + 1].append((r, c))

    ##########

    from collections import deque

    # root는 전부 탈출 가능한 칸
    count = len(roots)

    queue = deque()

    # root를 가지는 subtree의 모든 node는 탈출 가능한 칸이다.
    for r, c in roots:
        queue.append((r, c))

    # 별다른 조건 없이 순회, indexError는 graph 제작에서 전부 걸러졌음
    while queue:
        r, c = queue.popleft()

        for nr, nc in graph[r][c]:
            queue.append((nr, nc))
            count += 1

    print(count)

    ##########

    return


# [Review]

# 짜고 보니 순회라 하기도 귀엽다.
# graph 짜는 부분에 대한 최적화를 여러가지로 할 수 있었다.
# https://www.acmicpc.net/status?user_id=marigold2003&problem_id=17090&from_mine=1


if __name__ == "__main__":
    main()
