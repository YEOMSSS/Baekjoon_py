import sys

input = sys.stdin.readline


# 9등분 내서 가운데를 제외하고 재귀한다.
# 음, 굳이 board가 필요할까?
# 프랙탈구조를 응용해보자. 안으로 들어가는거지.


# "*" 하나를 3*3사이즈 테두리 별로 바꾸는 걸 재귀로 반복
def main3() -> None:
    def solve_R(n):
        if n == 1:
            return ["*"]

        rows = solve_R(n // 3)
        current = []

        for r in rows:  # ["***"]
            current.append(r * 3)
        for r in rows:  # ["* *"]
            current.append(r + " " * (n // 3) + r)
        for r in rows:  # ["***"]
            current.append(r * 3)

        return current

    N = int(input())
    for row in solve_R(N):
        print(row)


# 전체를 "*"로 시작해서 가운데를 " "으로 채운다.
def main2() -> None:
    N = int(input())

    answer = [["*"] * N for _ in range(N)]

    def draw(n, r, c):
        nonlocal answer

        for y in range(r, r + n):
            for x in range(c, c + n):
                answer[y][x] = " "

    def solve_R(n, r, c):

        if n == 1:
            return

        d3 = n // 3
        for dr in range(3):
            for dc in range(3):
                if dr == 1 and dc == 1:
                    draw(d3, r + d3, c + d3)
                else:
                    solve_R(d3, r + (dr * d3), c + (dc * d3))

    solve_R(N, 0, 0)
    for a in answer:
        print("".join(a))


# 전체를 " "로 시작해서 가운데의 테두리를 "*"으로 채운다.
def main() -> None:
    N = int(input())

    answer = [[" "] * N for _ in range(N)]

    def draw(n, r, c):
        nonlocal answer

        for y in range(r, r + n):
            for x in range(c, c + n):
                if y == r or x == c or y == r + n - 1 or x == c + n - 1:
                    answer[y][x] = "*"

    def solve_R(n, r, c):

        if n == 3:
            draw(n, r, c)
            return

        d3 = n // 3
        for dr in range(3):
            for dc in range(3):
                if dr == 1 and dc == 1:
                    continue
                solve_R(d3, r + (dr * d3), c + (dc * d3))

    solve_R(N, 0, 0)
    for a in answer:
        print("".join(a))


if __name__ == "__main__":
    main3()
