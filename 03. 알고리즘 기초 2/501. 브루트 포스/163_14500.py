'''
문제
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.



아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다.
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다.
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다.
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.

예제 입력 1 
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
예제 출력 1 
19
예제 입력 2 
4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
예제 출력 2 
20
예제 입력 3 
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
예제 출력 3 
7
'''

# 숫자판을 입력받는다.
# 이어진 4개의 수의 합 중 제일 큰 것 찾기.
'''
import sys
input = sys.stdin.readline

def main():

    ROW, COLUMN = map(int, input().split())

    num_board = [list(map(int, input().split())) for _ in range(ROW)]

    answer = 0

    # ㅁ
    for i in range(ROW - 1):
        for j in range(COLUMN - 1):
            answer = max(
                answer,
                num_board[i][j] + num_board[i][j + 1] + num_board[i + 1][j] + num_board[i + 1][j + 1]
            )
    # ㅣ
    for i in range(ROW - 3):
        for j in range(COLUMN):
            answer = max(
                answer,
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i + 3][j]
            )
    # ㅡ
    for i in range(ROW):
        for j in range(COLUMN - 3):
            answer = max(
                answer,
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i][j + 3]
            )
    # ㅗ파생
    for i in range(1, ROW):
        for j in range(COLUMN - 2):
            answer = max(
                answer,
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i - 1][j],
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i - 1][j + 1],
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i - 1][j + 2],
                num_board[i][j] + num_board[i][j + 1] + num_board[i - 1][j + 1] + num_board[i - 1][j + 2]
            )
    # ㅜ파생
    for i in range(ROW - 1):
        for j in range(COLUMN - 2):
            answer = max(
                answer,
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i + 1][j],
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i + 1][j + 1],
                num_board[i][j] + num_board[i][j + 1] + num_board[i][j + 2] + num_board[i + 1][j + 2],
                num_board[i][j] + num_board[i][j + 1] + num_board[i + 1][j + 1] + num_board[i + 1][j + 2]
            )
    # ㅏ파생
    for i in range(ROW - 2):
        for j in range(COLUMN - 1):
            answer = max(
                answer,
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i][j + 1],
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i + 1][j + 1],
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i + 2][j + 1],
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 1][j + 1] + num_board[i + 2][j + 1]
            )
    # ㅓ파생
    for i in range(ROW - 2):
        for j in range(1, COLUMN):
            answer = max(
                answer,
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i][j - 1],
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i + 1][j - 1],
                num_board[i][j] + num_board[i + 1][j] + num_board[i + 2][j] + num_board[i + 2][j - 1],
                num_board[i][j] + num_board[i + 1][j - 1] + num_board[i + 1][j] + num_board[i + 2][j - 1]
            )

    print(answer)

if __name__ == "__main__":
    main()
'''
# 일단 정리는 나중에 하고, 돌아가게만 해보자고.
# 굳이 범위를 다 나누지 말고 그냥 퉁쳐서 인덱스오류뜨면 continue하는 방식으로..

import sys
input = sys.stdin.readline

def main():
    ROW, COLUMN = map(int, input().split())

    num_board = [list(map(int, input().split())) for _ in range(ROW)]

    tetrominos = [
        # ㅁ
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        # ㅣ, ㅡ
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        # ㅗ 파생
        [(1, 0), (1, 1), (1, 2), (0, 0)],
        [(1, 0), (1, 1), (1, 2), (0, 1)],
        [(1, 0), (1, 1), (1, 2), (0, 2)],
        [(1, 0), (1, 1), (0, 1), (0, 2)],
        # ㅜ 파생
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        # ㅏ 파생
        [(0, 0), (1, 0), (2, 0), (0, 1)],
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        # ㅓ 파생
        [(0, 1), (1, 1), (2, 1), (0, 0)],
        [(0, 1), (1, 1), (2, 1), (1, 0)],
        [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 1), (1, 0), (1, 1), (2, 0)]
    ]

    answer = 0
    for i in range(ROW):
        for j in range(COLUMN):
            for tetromino in tetrominos:
                # 테트리스 모양을 그대로 가져와서 i, j 로 좌표만 수정한다.
                try:
                    # tetromino에 저장된 변화량을 가져온다.
                    total = sum(num_board[i + dx][j + dy] for dx, dy in tetromino)
                    answer = max(answer, total)
                except IndexError:
                    continue

    print(answer)

if __name__ == "__main__":
    main()

# 빠르긴 앞에게 훨씬 빠르다. 하드코딩의 위엄.