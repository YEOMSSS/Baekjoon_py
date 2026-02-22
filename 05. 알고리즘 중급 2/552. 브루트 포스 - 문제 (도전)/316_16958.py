# Authored by : marigold2003
# Date : 2026-02-22
# Link : https://www.acmicpc.net/problem/16958


import sys

input = sys.stdin.readline


# [Summary] 텔레포트

# N(1K)개의 도시들의 위치 정보가 주어진다. (x(1000), y(1000))
# 도시에서 도시로 이동하는 시간은 가로차+세로차
# 만약 두 도시가 모두 특별한 도시라면, 텔레포트로 T시간

# 두 도시의 쌍 M개가 주어질 때, 각 최소 이동 시간을 구하시오.


def main() -> None:

    # [Ideas]

    # 텔포를 쓰거나 안쓰거나 두 경우밖에 없다는 것을 알 수 있다.
    # 어차피 직접 걸어갈 때는 그냥 두 도시 사이 이동시간이 최소이고.

    # 만약 텔포를 쓴다면, 텔포를 두번 타는 경우는 의미가 없다.
    # 특별한 도시에서는 모든 특별한 도시로 이동 가능하므로, 두번 탈 필요가 없음.

    # 그러면 직접 이동하거나
    # 가장 가까운 텔포로 이동해서 목적지에 가장 가까운 텔포에 내려 목적지로 이동하기
    # 이 두 가지 경우밖에 없다는 것이다.

    # 결국 이 문제의 포인트는, 가장 가까운 텔포를 찾는 거임.
    # 이정도는 브루트포스로 찾을 수 있다.

    ##########

    N, T = map(int, input().split())

    cities = []
    special_cities = []
    for _ in range(N):
        s, x, y = map(int, input().split())
        cities.append((x, y))
        if s:
            special_cities.append((x, y))

    M = int(input())

    def direct_time(a: list[int], b: list[int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for _ in range(M):
        A, B = map(lambda x: cities[int(x) - 1], input().split())

        # A, B에 가장 가까운 텔포까지 가는 시간
        sp_A, sp_B = sys.maxsize, sys.maxsize
        for s in special_cities:
            sp_A = min(sp_A, direct_time(A, s))
            sp_B = min(sp_B, direct_time(B, s))

        result = min(direct_time(A, B), sp_A + T + sp_B)

        print(result)

    ##########

    return


# [Review]

# 특별한 도시가 없는 경우는? 어차피 maxsize라 걸러지고.
# 특별한 도시가 하나인 경우는? 무조건 direct가 더 빨라서 걸러지고.


if __name__ == "__main__":
    main()
