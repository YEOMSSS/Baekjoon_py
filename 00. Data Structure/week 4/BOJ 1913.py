# Authored by : marigold2003
# Date : 2026-03-25
# Link : https://www.acmicpc.net/problem/1913


import sys

input = sys.stdin.readline


# [Summary] 달팽이

# N*N(<= 999) board를 만들어야 한다.
# N은 홀수이며, board의 중심에는 1이 들어간다.
# 1 위에 2를 채우고, 시계방향으로 3,4,5... 순서로 채운 board를 출력하시오.


def main() -> None:

    # [Ideas]

    # 사실 좌측상단부터 N*N으로 시작하면 더 편하다.
    # 하우상좌 우선순위 방향으로 직진하면 되기 때문.

    # 하지만 중심에서부터 한번 나가보자.
    # 진행방향 기준 현재숫자의 우측이 차있으면 직진하고,
    # 차있지 않으면 우측으로 꺾어서 가면 된다.

    ##########

    # 우 하 좌 상. 사실 시계방향이기만 하면 된다.
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    N = int(input())
    K = int(input())

    board = [[0] * N for _ in range(N)]

    y, x = N // 2, N // 2
    num = 1

    board[y][x] = num
    num += 1

    # 꺾기 위해 좌측에서 시작
    dir = 2

    # 1의 좌표
    answer = (y + 1, x + 1)

    while num <= N * N:
        # 현재 좌표의 우측 검사, 없으면 직진, 있으면 우측으로 진행방향 꺾기
        right = (dir + 1) % 4
        if board[y + dy[right]][x + dx[right]] == 0:
            dir = right

        ny = y + dy[dir]
        nx = x + dx[dir]

        y, x = ny, nx
        board[y][x] = num

        # K의 좌표 저장
        if num == K:
            answer = (y + 1, x + 1)

        num += 1

    for row in board:
        print(*row)

    print(*answer)

    ##########

    return


# [Review]

# 중앙부터 펼쳐 나가는 것도 다양한 방법이 있을 것 같다.
# 굳이 8방향을 확인하지 않아도 쉽게 해결 가능.


if __name__ == "__main__":
    main()
