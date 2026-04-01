import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-04-01
# Problem Number : 4875


# [Summary] 4875. [S/W 문제해결 기본] 5일차 - 미로

# N*N(<= 100) board에 미로가 그려져 있다.
# 2에서 출발해서 3으로 도착해야 한다. 0은 통로, 1은 벽이다.
# 도착이 가능한지 판단하시오.


def main() -> None:

    # [Ideas]

    # 격자그래프 dfs를 사용하고 싶으나,
    # 좌표를 스택에 밀어넣는 방식으로 진행해보자.
    # 사실 논리는 똑같으니까.

    # 우하좌상으로 push해서 상좌하우로 pop하자.

    ##########

    # 우하좌상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().rstrip())) for _ in range(N)]

        for y in range(N):
            for x in range(N):

                if board[y][x] == 2:
                    start = (y, x)

        stack = []
        stack.append(start)

        flag = False
        # 스택이 비었다는 것은 더 이상 이동가능한 칸이 없다는 것이다.
        while stack:
            y, x = stack.pop()
            if board[y][x] == 3:
                flag = True
                break

            # 방문처리
            board[y][x] = 1

            for dir in range(4):
                ny, nx = y + dy[dir], x + dx[dir]

                if not (0 <= ny < N and 0 <= nx < N):
                    continue
                if board[ny][nx] == 1:
                    continue

                stack.append((ny, nx))

        print(f"#{tc} {1 if flag else 0}")

    ##########

    return


# [Review]

# dfs 문제를 푼 듯한 느낌이 든다.


if __name__ == "__main__":
    main()
