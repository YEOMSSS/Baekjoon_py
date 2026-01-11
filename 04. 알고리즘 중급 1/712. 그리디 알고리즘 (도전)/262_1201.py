import sys

input = sys.stdin.readline

# 1 2 3 4 5 LIS5 LDS1
# 1 2 3 5 4 LIS4 LDS2
# 1 2 5 4 3 LIS3 LDS3
# 1 5 4 3 2 LIS2 LDS4
# 5 4 3 2 1 LIS1 LDS5

# 2 1 3 4 5 LIS4 LDS2
# 2 1 3 5 4 LIS3 LDS2

# 1 2 3 4 5 6 7 8 9 LIS9 LDS1
# 2 1 3 4 5 6 7 8 9 LIS8 LDS2
# 2 1 3 4 5 6 7 9 8 LIS7 LDS2

# '2 1' '4 3' '6 5' '8 7' '9' LIS5 LDS2
# '3 2 1' '6 5 4' '9 8 7' LIS3 LDS3
# 이런느낌이구만.
# 묶음의 개수가 LIS의 길이, 묶음의 최대길이가 LDS의 길이다.
# M*K가 N보다 작으면 못 만든다. 둘이 곱해서 최소가 되게 해도 N과 같거나 크니까.

# 근데 M과 K가 무작정 크면 어떡하지?
# M+K의 최대값이 N+1이니까, N은 M+K-1보다 크거나 같아야 한다.


def main() -> None:

    # 길이, LIS길이, LDS길이
    N, M, K = map(int, input().split())

    # 1 2 3 4 5 6 LIS6 LDS1
    # M+K의 최대값은 N+1이다. N은 M+K-1보다 크거나 같아야 한다.
    if N < M + K - 1:
        print(-1)
        return

    # 2 1 4 3 6 5 LIS3 LDS2
    # M*K는 N보다 크거나 같아야 한다.
    if N > M * K:
        print(-1)
        return

    # 우선 LDS를 만든다.
    print(*range(K, 0, -1), end=" ")

    # N-K개의 수로 M-1개의 묶음을 만들어야 한다.
    N -= K
    M -= 1

    while M:
        # 앞으로 사용해야 할 수를 만들어야 할 묶음의 수로 나눠 이번 묶음의 길이를 구한다.
        use_current = N // M
        print(*range(K + use_current, K, -1), end=" ")
        K += use_current  # 다음 수의 시작이 이번에 사용한 N//K만큼 더해진다.
        N -= use_current  # 앞으로 사용해야 할 수는 N//K만큼 줄어든다.
        M -= 1  # 묶음을 하나 만들었으니 앞으로 만들어야 할 묶음의 수를 줄인다.


if __name__ == "__main__":
    main()
