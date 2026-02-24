# Authored by : marigold2003
# Date : 2026-02-24
# Link : https://www.acmicpc.net/problem/16957


import sys

input = sys.stdin.readline


# [Summary] 체스판 위의 공

# R(500)*C(500) board가 있고, 각 칸에는 정수가 하나씩 적혀있다.
# 모든 정수는 서로 다르다.

# 각 칸 위에 공이 하나씩 놓여 있으며, 공은 규칙에 의해 자동으로 움직인다.
# 인접 8방향의 모든 정수가 현재 칸의 정수보다 크면 이동을 멈춘다.
# 그 외의 경우, 가장 적은 정수가 있는 칸으로 이동한다.

# 한 칸 위에 여러 개의 공이 있을 수 있다.
# 공이 더 이상 움직이지 않을 때, 각 칸에 공이 몇 개 있는지 구하시오.


def main() -> None:

    # [Ideas]

    # 뭐야, graph 구현이잖아.
    # 모든 칸에서 전부 simulation하고 result를 나타내면 된다.

    # 그런데 하다 보니... 이거, tree문제느낌이 난다.
    # 이동불가한 칸을 root로 하여 그 tree를 순회하면 된다.
    # 그럼 또 graph를 거꾸로 만들어야겠네. #17090이 생각난다.
    # 역시 visited는 필요 없겠다.

    ##########

    MAX_VAL = 300_001
    R, C = map(int, input().split())
    
    # padding으로 index 처리
    board = (
        [[MAX_VAL] * (C + 2)]
        + [[MAX_VAL] + list(map(int, input().split())) + [MAX_VAL] for _ in range(R)]
        + [[MAX_VAL] * (C + 2)]
    )

    # [row][col][neighbors]
    graph = [[[] for _ in range(C)] for _ in range(R)]
    roots = []

    # 상하좌우 좌상우상좌하우하
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

    for r in range(1, R + 1):
        for c in range(1, C + 1):

            curr = board[r][c]
            min_r, min_c = r, c

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                nei = board[nr][nc]

                if nei < curr:
                    curr = nei
                    min_r, min_c = nr, nc

            if (min_r, min_c) != (r, c):
                graph[min_r - 1][min_c - 1].append((r - 1, c - 1))
            else:
                roots.append((r - 1, c - 1))

    ##########

    from collections import deque

    counts = [[0] * C for _ in range(R)]

    # root는 이동 불가능한 칸, 각 tree의 node 개수 세기
    for root_r, root_c in roots:

        queue = deque()

        count = 1
        queue.append((root_r, root_c))

        while queue:
            r, c = queue.popleft()

            for nr, nc in graph[r][c]:
                queue.append((nr, nc))
                count += 1

        counts[root_r][root_c] = count

    for row in counts:
        print(*row)

    ##########

    return


# [Review]

# forest를 보라.


if __name__ == "__main__":
    main()
