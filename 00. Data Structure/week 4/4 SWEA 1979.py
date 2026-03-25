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
# Problem Number : 1979


# [Summary] 1979. 어디에 단어가 들어갈 수 있을까

# 0과 1로 이뤄진 N*N(5 <= N <= 15) board가 주어진다.
# 1이 K만큼 직선으로 연속된 것이 몇 개 있는지 구하시오.


def main() -> None:

    # [Ideas]

    # 행마다 1의 연속을 찾고, 열마다 1의 연속을 찾자.
    # 행기준 완탐 한번, 열기준 완탐 한번 할까.

    # 수업에서는 전치행렬을 만들어서 한번 다시 돌렸다.

    ##########

    T = int(input())

    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]

        answer = 0

        # 행 기준 완탐
        for y in range(N):
            count = 0
            for x in range(N):

                # 1이면 연속 카운트 시작
                if board[y][x] == 1:
                    count += 1

                # 0이면 K연속인지 확인 후 초기화
                else:
                    if count == K:
                        answer += 1
                    count = 0

            # 행이 끝났을 때도 갱신 필요
            if count == K:
                answer += 1
        """
        # 열 기준 완탐
        for x in range(N):
            count = 0
            for y in range(N):

                # 1이면 연속 카운트 시작
                if board[y][x] == 1:
                    count += 1

                # 0이면 K연속인지 확인 후 초기화
                else:
                    if count == K:
                        answer += 1
                    count = 0

            # 행이 끝났을 때도 갱신 필요
            if count == K:
                answer += 1
        """

        # 전치행렬을 만들어서 다시 완탐한다.
        board2 = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                board2[y][x] = board[x][y]

        for y in range(N):
            count = 0
            for x in range(N):

                # 1이면 연속 카운트 시작
                if board2[y][x] == 1:
                    count += 1

                # 0이면 K연속인지 확인 후 초기화
                else:
                    if count == K:
                        answer += 1
                    count = 0

            # 행이 끝났을 때도 갱신 필요
            if count == K:
                answer += 1

        print(f"#{tc} {answer}")

        # 아 합치고 싶다. 아 합치고 싶다.
        # 똑같은거 두개 있으니까 너무 불편하다.

    ##########

    return


# [Review]

# 완탐 두번 하는게 나름 효율적이다.


if __name__ == "__main__":
    main()
