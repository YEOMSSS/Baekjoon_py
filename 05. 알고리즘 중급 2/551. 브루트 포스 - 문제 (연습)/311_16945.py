# Authored by : marigold2003
# Date : 2026-02-16
# Link : https://www.acmicpc.net/problem/16945


import sys

input = sys.stdin.readline


# [Summary] 매직 스퀘어로 변경하기

# 3*3 배열이 입력된다. 입력된 배열을 마방진으로 바꿔야 한다.
# 값을 a에서 b로 바꾸는 비용은 |a-b| 이다.
# 마방진으로 변경하는 비용의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 3*3 마방진은 8종류다.
    # 그니까 원래 하난데, 돌리고 뒤집어서 8개.
    # 다 하나씩 비교해보지 뭐.

    ##########

    magic_square = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]

    board = [num for _ in range(3) for num in map(int, input().split())]

    answer = sys.maxsize

    for ms in magic_square:
        # lambda로 빠르게 처리하기
        cost = sum(map(lambda x, y: abs(x - y), ms, board))
        answer = min(answer, cost)

    print(answer)

    ##########

    return


# [Review]

# 마방진이 매직스퀘어여? 그렇구나.


if __name__ == "__main__":
    main()
