# Authored by : marigold2003
# Date : 2026-03-02
# Link : https://www.acmicpc.net/problem/16956


import sys

input = sys.stdin.readline


# [Summary] 늑대와 양

# R(500)*C(500) board에 늑대와 양이 있다.
# 울타리를 설치해서 늑대가 양이 있는 칸으로 가지 못하게 해야 한다.
# 가능할 경우 울타리를 설치하시오.


def main() -> None:

    # [Ideas]

    # 울타리 수가 제한이 없다.
    # 그냥 양 주변을 울타리로 감싸면 됨.
    # 만약 양과 늑대가 붙어있다면 불가능이지 뭐.

    # padding을 해서 이득이 생길까?
    # 이정도는 그냥 인덱스판정하는게 출력하기도 편하지 않을까?

    ##########

    R, C = map(int, input().split())
    # temp = ["."] * (C + 2)
    # board = [temp, ["."] + list(list(input().rstrip()) for _ in range(R)) + ["."], temp]

    board = [list(input().rstrip()) for _ in range(R)]

    for r in range(R):
        for c in range(C):
            curr = board[r][c]

            # 양 찾기
            if curr == "S":

                # 양을 감싸는 울타리 놓기
                for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C:
                        continue

                    nei = board[nr][nc]
                    # 늑대가 옆에 있으면 불가능
                    if nei == "W":
                        print(0)
                        return

                    # 울타리를 놓을 수 있으면 놓는다.
                    if nei == ".":
                        board[nr][nc] = "D"

    print(1)
    for row in board:
        print("".join(row))

    ##########

    return


# [Review]

# 문제 노트가 친절하다.
# 없어도 그렇게까지 발상이 어렵진 않음.

# 아, 울타리 가득이어도 되네? ;;;;;


if __name__ == "__main__":
    main()
