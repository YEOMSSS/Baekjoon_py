import sys

input = sys.stdin.readline


# 2447번을 그대로 응용해보자.
# 다만 이번엔 첫 삼각형 모양은 주어지게 해둬야할 듯.
def main() -> None:

    def solve_R(n):

        if n == 3:
            return ["  *  ", " * * ", "*****"]

        n //= 2
        rows = solve_R(n)
        current = []

        for r in rows:
            current.append(" " * n + r + " " * n)
        for r in rows:
            current.append(r + " " + r)

        return current

    N = int(input())
    for row in solve_R(N):
        print(row)


if __name__ == "__main__":
    main()
