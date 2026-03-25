import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-03-25
# Problem Number : 1954


# [Summary] 1954. 달팽이 숫자

# N*N(<= 10) board가 있다.
# 좌측 상단부터 1로 시작해서 시계방향으로 숫자를 배치한다.
# 완성된 board를 출력하시오.


def main() -> None:

    # [Ideas]

    # 방향에 우선순위를 둔다.
    # 우, 하, 좌, 상 순서로 놓는다.
    # 직진하다가 막히면 다음 방향을 시도한다.
    # 뚫렸다면 직진.

    ##########

    T = int(input())

    # 우 하 좌 상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    def isSafe(y, x, N) -> bool:
        return 0 <= y < N and 0 <= x < N

    for tc in range(1, T + 1):
        print(f"#{tc}")

        N = int(input())
        board = [[0] * N for _ in range(N)]

        y, x = 0, 0
        num = 1

        board[y][x] = num
        num += 1

        # 숫자는 N*N까지만
        while num <= N * N:

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                flag = False

                while isSafe(ny, nx, N) and board[ny][nx] == 0:
                    y, x = ny, nx
                    board[y][x] = num
                    num += 1

                    ny += dy[dir]
                    nx += dx[dir]

                    flag = True

                if flag:
                    break

        for row in board:
            print(*row)

    ##########

    return


# [Review]

# curr coord의 갱신 타이밍이 포인트.


if __name__ == "__main__":
    main()
