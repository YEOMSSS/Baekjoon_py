import sys

input = sys.stdin.readline


# 341을 좌표로 바꾼 후 2,1만큼 움직여서 분할정복하면 되지 않을까?


def main() -> None:
    d, num = input().split()
    d = int(d)

    # 오른쪽으로 x, 위로 y
    x, y = map(int, input().split())

    r, c = 0, 0
    for n in num:
        r *= 2
        c *= 2

        match n:
            case "2":
                pass
            case "1":
                c += 1
            case "3":
                r += 1
            case "4":
                r += 1
                c += 1

    # 1074번에서 가져와서 사분면을 출력하고 그 사분면으로 들어가도록 개조
    answer = ""

    def solve_R(n, r, c) -> None:
        nonlocal answer

        if not n:
            return

        half_length = 2 ** (n - 1)

        # 위쪽 칸일 때
        if r < half_length:

            # 좌상일 때
            if c < half_length:
                answer += "2"
                solve_R(n - 1, r, c)

            # 우상일 때
            else:  # c >= half_length
                answer += "1"
                solve_R(n - 1, r, c - half_length)

        # 아래쪽 칸일 때
        else:  # r >= half_length

            # 좌하일 때
            if c < half_length:
                answer += "3"
                solve_R(n - 1, r - half_length, c)

            # 우하일 때
            else:  # c >= half_length
                answer += "4"
                solve_R(n - 1, r - half_length, c - half_length)

    tr, tc = r - y, c + x
    if tr < 0 or 2**d <= tr or tc < 0 or 2**d <= tc:
        print(-1)
        return

    solve_R(d, tr, tc)
    print(answer)


if __name__ == "__main__":
    main()

# 풀고 나니, 사분면을 좌표로 바꿀 때 재귀를 사용하지 않았는데
# 좌표를 사분면으로 바꿀 때도 재귀 쓸 필요 없는 거 아냐?
