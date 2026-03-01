# Authored by : marigold2003
# Date : 2026-02-28
# Link : https://www.acmicpc.net/problem/1208


import sys

input = sys.stdin.readline


# [Summary] 부분수열의 합 2

# N(40)개의 정수(100K)로 이루어진 수열이 있다.
# sum(부분수열) == S(abs(1M))가 되는 경우의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 중간에서 만나기를 배워보자. meet in the middle
    # 통짜 bruteforce 돌리면 2**40이라 그냥 말이 안됨.
    # 배열을 반으로 갈라서 2**20 + 2**20으로 부분수열의 합 배열을 두개 만든다.
    # 2**20 = 1048576 쌉가능이다.

    # 그리고 한쪽을 정렬해서 다른 한쪽의 모든 원소에 이분탐색.
    # 대충 이분탐색 1M * (log2 20) = 20M. 아슬한가
    # 투포인터 돌려도 될거같은디? 구현은 이분탐색이 더 편하네.

    # 중복되는 것들을 다 횟수에 포함해야 한다.
    # 이분탐색은 중복 카운트는 안해주니까.

    ##########

    from itertools import combinations

    N, S = map(int, input().split())
    arr = tuple(map(int, input().split()))

    mid = N // 2
    val = arr[:mid]
    right = arr[mid:]

    Lsum = [sum(comb) for k in range(len(val) + 1) for comb in combinations(val, k)]
    Rsum = [sum(comb) for k in range(len(right) + 1) for comb in combinations(right, k)]
    Rsum.sort()

    from bisect import bisect_left, bisect_right

    count = 0
    for val in Lsum:
        target = S - val

        # 중복을 다 세야하니까, bleft랑 bright를 다 갖다써야한다.
        # target이 배열에 없으면 left == right가 된다.

        # target의 처음 등장 위치
        left = bisect_left(Rsum, target)
        # target의 마지막 등장 다음 위치
        right = bisect_right(Rsum, target)

        count += right - left

    # 공집합 + 공집합은 제외해야 한다.
    # 문제 조건에서 부분수열의 크기는 양수임.
    if S == 0:
        count -= 1

    print(count)

    ##########

    return


# [Review]

# meet-in-the-middle 배워보기. mitm
# bsearch가 좋긴 좋아.


if __name__ == "__main__":
    main()
