import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-04-14
# Problem Number : 12712


# [Summary] 12712. 파리퇴치3

# N*N(<= 15) board의 각 칸마다 파리가 몇 마리씩 앉아 있다.
# M(<= N) 크기의 스프레이를 + 또는 x 형태로 분사할 수 있다.
# 스프레이 한 번에 잡을 수 있는 가장 많은 파리의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 브루트포스 시뮬레이션이지.
    # dr dc 만들어놓고 하면 된다. +버전이랑 x버전 두개.

    ##########

    T = int(input())

    # +는 상하좌우
    dr_cross = [-1, 1, 0, 0]
    dc_cross = [0, 0, -1, 1]

    # x는 좌상 좌하 우상 우하
    dr_xshape = [-1, 1, -1, 1]
    dc_xshape = [-1, -1, 1, 1]

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]

        answer = 0

        for r in range(N):
            for c in range(N):

                # +자부터
                sum = board[r][c]
                for m in range(1, M):
                    for dir in range(4):
                        nr, nc = r + dr_cross[dir] * m, c + dc_cross[dir] * m
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        sum += board[nr][nc]
                answer = max(answer, sum)

                # 이후 x자도 확인
                sum = board[r][c]
                for m in range(1, M):
                    for dir in range(4):
                        nr, nc = r + dr_xshape[dir] * m, c + dc_xshape[dir] * m
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        sum += board[nr][nc]
                answer = max(answer, sum)

        print(f"#{tc} {answer}")

    ##########

    return


# [Review]

# 최적화를 더 할 수 있긴 하다.
# 십자의 한 방향씩 while로 돌리면 된다.


if __name__ == "__main__":
    main()
