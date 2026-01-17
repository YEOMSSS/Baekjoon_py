import sys

input = sys.stdin.readline


# 칸을 계속 4등분내서 앞칸들을 더해주는 식으로 가면 되지 않을까?
# 4등분된 칸을 큰 칸 하나로 치고 또 그 안에서 4등분.


def main() -> None:
    N, r, c = map(int, input().split())

    count = 0

    def solve_R(N, r, c) -> None:
        nonlocal count

        if not N:
            return

        half_length = 2 ** (N - 1)

        # 위쪽 칸일 때
        if r < half_length:

            # 좌상일 때
            if c < half_length:
                solve_R(N - 1, r, c)

            # 우상일 때
            else:  # c >= half_length
                count += half_length**2
                solve_R(N - 1, r, c - half_length)

        # 아래쪽 칸일 때
        else:  # r >= half_length

            # 좌하일 때
            if c < half_length:
                count += half_length**2 * 2
                solve_R(N - 1, r - half_length, c)

            # 우하일 때
            else:  # c >= half_length
                count += half_length**2 * 3
                solve_R(N - 1, r - half_length, c - half_length)

    # 재귀는 N + 1회 작동한다.
    solve_R(N, r, c)
    print(count)


if __name__ == "__main__":
    main()

# 나이스~~
