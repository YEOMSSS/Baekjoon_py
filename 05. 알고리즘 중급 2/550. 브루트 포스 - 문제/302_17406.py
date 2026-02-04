# Authored by : marigold2003
# Date : 2026-02-04
# Link : https://www.acmicpc.net/problem/17406

import sys

input = sys.stdin.readline


# [Summary]

# 회전 연산이 최대 6회 주어진다. 회전연산의 순서는 상관 없다.
# 회전 연산은 (r, c, s)이다. r, c를 중심으로 정사각형을 s만큼 거리에 그린다.
# 회전은 시계방향으로 돌려주면 된다.

# 모든 회전 연산을 완료했을 때 배열의 값의 최솟값을 구하여라.
# 배열의 값은 배열의 각 행의 합 중 최솟값이다.


def main() -> None:

    # [Ideas]

    # 다 해보면 되지 뭐. 회전 6번밖에 안되는데
    # 6! = 720 적다 적어.

    # 결국 회전을 구현하는 구현 문제인 것이다.

    ##########

    N, M, K = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(N))
    commands = tuple(tuple(map(int, input().split())) for _ in range(K))

    from itertools import permutations

    answer = sys.maxsize

    for perm in permutations(range(K)):

        # 2차원보드 깊은복사
        curr_board = list(map(list, board))
        for p in perm:

            # 회전
            r, c, s = commands[p]
            r -= 1
            c -= 1

            for i in range(1, s + 1):
                # 좌상단을 임시 저장
                lu = curr_board[r - i][c - i]

                # 왼쪽을 위로
                for nr in range(r - i, r + i):
                    curr_board[nr][c - i] = curr_board[nr + 1][c - i]
                # 아래를 왼쪽으로
                curr_board[r + i][c - i : c + i] = curr_board[r + i][c - i + 1 : c + i + 1] # fmt: skip
                # 오른쪽을 아래로
                for nr in range(r + i, r - i, -1):
                    curr_board[nr][c + i] = curr_board[nr - 1][c + i]
                # 위를 오른쪽으로
                curr_board[r - i][c - i + 1 : c + i + 1] = curr_board[r - i][c - i : c + i] # fmt: skip

                # 좌상단을 이동한 위치에 다시 넣기
                curr_board[r - i][c - i + 1] = lu

        temp = min(sum(row) for row in curr_board)
        answer = min(answer, temp)

    print(answer)

    ##########

    return


# [Review]

# 아, rotate 써볼걸

if __name__ == "__main__":
    main()
