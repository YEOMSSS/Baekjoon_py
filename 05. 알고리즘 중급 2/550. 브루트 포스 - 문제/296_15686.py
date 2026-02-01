# Authored by : marigold2003
# Date : 2026-01-31
# Link : https://www.acmicpc.net/problem/15686

import sys

input = sys.stdin.readline


# [Summary]

# 치킨집과 집이 있는 2차원 보드가 주어진다.
# 각 집에서 가장 가까운 치킨집까지의 거리를 치킨 거리라고 한다.
# 치킨집을 M개만 남기고 없앴을 때, 모든 집의 치킨 거리의 합의 최솟값을 구하시오.


def main():

    # [Ideas]

    # 집은 최대 100채. 치킨집은 최대 13곳.
    # 우선 조합으로 살릴 치킨집을 뽑아낸다.
    # 모든 집에서 치킨 거리를 구하면서 최솟값을 갱신한다.

    ##########

    from itertools import combinations

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    houses = set()
    chickens = set()

    for r in range(N):
        for c in range(N):
            curr = board[r][c]
            if curr == 1:
                houses.add((r, c))
            elif curr == 2:
                chickens.add((r, c))

    answer = sys.maxsize

    # 치킨집 조합 뽑기
    for comb in combinations(chickens, M):

        total = 0

        # 각 집의 치킨 거리 구하기
        for hr, hc in houses:

            min_dist = N * 2

            for cr, cc in comb:
                min_dist = min(min_dist, (abs(hr - cr) + abs(hc - cc)))

            total += min_dist

        answer = min(answer, total)

    print(answer)

    ##########

    return


# [Review]

# 쉽고 빠른 브루트포스
# 인덱스로 모든게 해결되어 편하다.

if __name__ == "__main__":
    main()
