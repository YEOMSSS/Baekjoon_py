import sys

input = sys.stdin.readline


# 1 2 3
# 2 4 6
# 3 6 9

# 1 2 2 3 3 4 6 6 9
# 1 2 3 4 5 6 7 8 9
# 순서는 항상 자신의 값보다 크거나 같다.


# 값의 순서로 판정하는 이분탐색
def b_search(N, K):
    left = 1
    right = K  # N*N

    # 줄여가면서 찾을 것이다.
    result = right

    while left <= right:
        mid = (left + right) // 2

        rank = 0
        # 모든 행에 대하여 순서를 누적
        for i in range(1, N + 1):
            # 행을 i로 나누면 1,2,3,...,N의 형태가 된다.
            # mid//i보다 작은 값들의 최대치는 N개다.
            rank += min(N, mid // i)

        # rank는 mid보다 작거나 같은 값의 개수다.
        # rank는 K보다 크거나 같아야 한다.
        # 이 문제는 K보다 많은 값을 앞에 둔 최솟값을 찾는 문제다. 아하! 이거네

        # rank가 K보다 높으면 mid를 줄여본다.
        if rank >= K:
            right = mid - 1
            result = mid
        # rank가 K보다 낮으면 mid를 늘려야만 한다.
        else:
            left = mid + 1

    return result


def main() -> None:
    N = int(input())
    K = int(input())

    print(b_search(N, K))


if __name__ == "__main__":
    main()
