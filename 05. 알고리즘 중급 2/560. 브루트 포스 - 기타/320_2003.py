# Authored by : marigold2003
# Date : 2026-02-26
# Link : https://www.acmicpc.net/problem/2003


import sys

input = sys.stdin.readline


# [Summary] 수들의 합 2

# N(10K)개로 된 수열 A가 있다.
# sum(A[i:j+1])가 M이 되는 경우의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 투포인터인가.

    ##########

    N, M = map(int, input().split())
    arr = tuple(map(int, input().split()))

    curr_sum = 0
    count = 0

    # 투포인터를 for문으로 관리
    end = 0
    for start in range(N):

        while curr_sum < M and end < N:
            curr_sum += arr[end]
            end += 1

        if curr_sum == M:
            count += 1

        curr_sum -= arr[start]

    print(count)

    ##########

    return


# [Review]

# 생각보다 어렵네.
# 이것도 기초개념이 탄탄해야겠다.


if __name__ == "__main__":
    main()
