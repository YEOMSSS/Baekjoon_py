# Authored by : marigold2003
# Date : 2026-01-29
# Link : https://www.acmicpc.net/problem/15683

import sys

input = sys.stdin.readline


# [Summary]

# CCTV 배치도가 있고, 최소 사각지대를 찾는다.
# 8*8사이즈의 보드까지 들어온다. CCTV도 최대 8개.
# CCTV는 모양이 정해져 있으며, 90도로 회전이 가능하다.
# 1은 -자, 2는 ㅡ자, 3은 ㄴ자, 4는 ㅗ자, 5는 +자.


def main():

    # [Ideas]

    # 보드도 작고, CCTV도 적다.
    # 그냥 브루트포스 돌리면 된다.
    # 구현만 좀 신경쓰면 될 듯.

    # 8개의 CCTV로 만드는 모든 경우는 회전방향4**8 = 65536가지
    # 5+는 회전이 필요없고, 2ㅡ는 두가지 경우만 확인하면 된다.
    # set으로 확인가능한 좌표를 저장하고, 벽까지 더해서 전체에서 빼면 사각지대.

    ##########

    from itertools import product

    # 세로길이, 가로길이
    N, M = map(int, input().split())
    board = tuple(tuple(map(int, input().split())) for _ in range(N))

    CCTVs = []
    walls = set()

    for r in range(N):
        for c in range(M):

            match board[r][c]:
                case 0:
                    pass

                # 벽 좌표 따로 모으기
                case 6:
                    walls.add((r, c))

                # CCTV마다 0상 1우 2하 3좌 방향에 대한 탐색범위 저장
                # 벽을 포함하지 않게 했다.
                case _:
                    temp = list(set() for _ in range(4))
                    # 상단
                    for nr in range(r, -1, -1):
                        if board[nr][c] == 6:
                            break
                        temp[0].add((nr, c))
                    # 우측
                    for nc in range(c, M):
                        if board[r][nc] == 6:
                            break
                        temp[1].add((r, nc))
                    # 하단
                    for nr in range(r, N):
                        if board[nr][c] == 6:
                            break
                        temp[2].add((nr, c))
                    # 좌측
                    for nc in range(c, -1, -1):
                        if board[r][nc] == 6:
                            break
                        temp[3].add((r, nc))

                    CCTVs.append(temp + [board[r][c]])

    answer = N * M
    CCTV_count = len(CCTVs)

    # 0, 1, 2, 3으로 CCTV 개수만큼 중복순열 구현하기
    for pro in product(range(4), repeat=CCTV_count):

        # 일단 벽을 집어넣어둔다.
        temp = set() | walls

        # CCTV 경로 탐색
        for i, p in enumerate(pro):

            # 일단 주어진 p방향은 무조건 확인한다.
            temp.update(CCTVs[i][p])

            match CCTVs[i][-1]:
                # p 반대방향을 추가
                case 2:
                    temp.update(CCTVs[i][(p + 2) % 4])
                # p 다음방향을 추가
                case 3:
                    temp.update(CCTVs[i][(p + 1) % 4])
                # p 다음방향, 아래방향을 추가
                case 4:
                    temp.update(CCTVs[i][(p + 2) % 4])
                    temp.update(CCTVs[i][(p + 1) % 4])
                # 전부 추가
                case 5:
                    temp.update(CCTVs[i][(p + 1) % 4])
                    temp.update(CCTVs[i][(p + 2) % 4])
                    temp.update(CCTVs[i][(p + 3) % 4])

        answer = min(answer, N * M - len(temp))

    print(answer)

    ##########

    return


# [Review]

# 그냥 빡구현 문제인 것 같음
# 이게 맞나 싶네. 너무 막 짰다. 최적화를 하지 않았다.
# 구석에 3, 4, 5번 CCTV가 있는 경우는 조합에 포함할 필요가 없기도 하고.
# 5번이나 2번 CCTV의 경우 조합을 더 줄일 수 있을 듯.

if __name__ == "__main__":
    main()
