# Authored by : marigold2003
# Date : 2026-03-09
# Link : https://www.acmicpc.net/problem/10811


import sys

input = sys.stdin.readline


# [Summary] 바구니 뒤집기

# 바구니가 N(<=100)개 있다. 1~N의 번호가 적혀 있다.
# 순서를 역순으로 바꿀 범위가 주어질 때, 결과를 출력하시오.


def main() -> None:

    # [Ideas]

    # [::-1]이나 .reverse()를 사용하면 된다.

    ##########

    N, M = map(int, input().split())
    baskets = list(range(1, N + 1))

    for _ in range(M):
        start, end = map(int, input().split())

        dummy = baskets[start - 1 : end]
        dummy.reverse()
        baskets[start - 1 : end] = dummy

        # baskets[start - 1 : end] = baskets[start - 1 : end][::-1]

    print(*baskets)

    ##########

    return


# [Review]

# 오랜만에 복습하기.


if __name__ == "__main__":
    main()
