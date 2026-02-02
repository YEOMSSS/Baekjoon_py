# Authored by : marigold2003
# Date : 2026-02-01
# Link : https://www.acmicpc.net/problem/2422

import sys

input = sys.stdin.readline


# [Summary]

# 아이스크림이 N종류가 있고, 같이 먹을 수 없는 조합이 주어진다.
# 제외하고 3가지 선택했을 때 경우의 수가 몇 가지인지 구하시오.


def main():

    # [Ideas]

    # 모든 경우에 대해 같이 먹을 수 없는 조합이 포함되는지 보면 된다.
    # 브루트포스지, 뭐.

    # 3중포문을 이용해 a,b가 벤이면 c를 확인하지 않게 직접 제어하자.

    # 난 멍청했다. 벤 목록을 조합에 비교하는게 아니라
    # 조합에서 ab ac bc를 뽑아 벤 목록에 들어있는지 확인하는 문제였다.

    ##########

    # 아이스크림 N종류, 금지 조합 M개
    N, M = map(int, input().split())
    banned = set(tuple(sorted(map(int, input().split()))) for _ in range(M))

    count = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):

            if (i, j) in banned:
                continue

            for k in range(j + 1, N + 1):

                if (i, k) in banned:
                    continue
                if (j, k) in banned:
                    continue

                count += 1

    print(count)

    ##########

    return


def main_comb():

    from itertools import combinations

    N, M = map(int, input().split())
    banned = set(tuple(sorted(map(int, input().split()))) for _ in range(M))

    count = 0

    for comb in combinations(range(1, N + 1), 3):
        if (comb[0], comb[1]) in banned:
            continue
        if (comb[0], comb[2]) in banned:
            continue
        if (comb[1], comb[2]) in banned:
            continue
        count += 1

    print(count)

    return


# [Review]

# 브루트포스도 생각을 해야 한다는 것을 배웠다.
# 무지성 거인이 되지 말자.

if __name__ == "__main__":
    # main()
    main_comb()
