# Authored by : marigold2003
# Date : 2026-02-27
# Link : https://www.acmicpc.net/problem/1806

import sys

input = sys.stdin.readline


# [Summary] 부분합

# 10K 이하 자연수로 이루어진 길이 N(100K)짜리 수열이 있다.
# 이 수열의 연속된 수들의 부분합 중 그 합이 S(100M) 이상이 되는 것 중
# 가장 짧은 것의 길이를 구하시오.


def main() -> None:

    # [Ideas]

    # 일단 누적합은 무조건 써야겠지.

    # 그런데 이거, 전부 확인해야 하나?
    # 조합으로 가면 너무 많아지는데. 100K**2 는 좀...

    # 그러면 답은 투포인터지 뭐... 기어가면 된다.

    ##########

    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 100001

    curr_sum = 0
    end = 0

    for start in range(N):

        # 현재 합이 S보다 작으면 오른쪽으로 늘려보자.
        # 단, 늘릴 수 있을 때만 늘리자.
        while curr_sum < S and end < N:
            curr_sum += arr[end]
            end += 1

        # 합이 target보다 같거나 클 때, 즉 조건만족시 실행
        if curr_sum >= S:
            answer = min(answer, end - start)

        curr_sum -= arr[start]

    print(answer if answer != 100001 else 0)

    ##########

    return


# [Review]

# 투포인터가 생각보다 유용하네.
# for문으로 start 굴리는 이 템플릿을 잘 익혀두자.


if __name__ == "__main__":
    main()
