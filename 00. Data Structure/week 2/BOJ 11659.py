# Authored by : marigold2003
# Date : 2026-03-11
# Link : https://www.acmicpc.net/problem/11659


import sys

# sys.stdin = open(
#     r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\week 2\input.txt",
#     "r",
# )
input = sys.stdin.readline


# [Summary] 구간 합 구하기 4

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하시오.


def main() -> None:

    # [Ideas]

    # 문제 생긴게 누적합같이 생겼다.
    # 일단 내장함수로 풀고, 수업대로 하자.

    ##########

    # accumulate를 알고 있다면?
    """
    from itertools import accumulate

    N, M = map(int, input().split())
    acc = list(accumulate(map(int, input().split()), initial=0))

    for _ in range(M):
        start, end = map(int, input().split())
        print(acc[end] - acc[start - 1])
    """

    # accumulate를 모른다면?
    howmany, quizNo = map(int, input().split())
    Data = list(map(int, input().split()))

    preSum = [0]
    sofar = 0
    for i in Data:
        sofar += i
        preSum.append(sofar)

    for _ in range(quizNo):
        start, end = map(int, input().split())

        # O(N*M) 쌩 sum은 불가능
        # print(sum(Data[start - 1 : end]))
        print(preSum[end] - preSum[start - 1])

    ##########

    return


# [Review]

# 그냥 sum으로는 당연히 불가능. pypy로도 시간초과 O(N*M)
# 누적합 배열을 사용해야 한다.


if __name__ == "__main__":
    main()
