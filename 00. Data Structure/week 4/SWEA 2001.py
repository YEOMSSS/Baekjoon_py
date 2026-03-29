import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-03-29
# Problem Number : 2001


# [Summary] 2001. 파리 퇴치

# N*N(<= 15) board에 랜덤한 값이 들어가 있다.
# M*M(<= N) 영역 내부 값의 총합의 최댓값을 구하시오.


def main() -> None:

    # [Ideas]

    # 문제가 누적합처럼 생겼다.
    # 2주차에 풀었던 백준 11659번이 생각난다.
    # row마다 누적합을 구해놓으면 편할 것 같은데? 하지만 좀 더 가보자.
    # 이번엔 누적합을 2차원 배열로 만들어서 풀어보자.

    ##########

    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())

        board = [list(map(int, input().split())) for _ in range(N)]
        # acc[y][x]는 (0,0) ~ (y,x) 직사각형 범위 전체 val의 합이 된다.
        acc = [[0] * (N + 1) for _ in range(N + 1)]

        for y in range(1, N + 1):
            for x in range(1, N + 1):
                # 이건 그림으로 그려보면 쉽다.
                acc[y][x] = (
                    board[y - 1][x - 1]
                    + acc[y - 1][x]
                    + acc[y][x - 1]
                    - acc[y - 1][x - 1]
                )

        max_result = 0
        # 누적합에서 원하는 범위를 꺼내기
        for y in range(M, N + 1):
            for x in range(M, N + 1):
                max_result = max(
                    max_result,
                    # 이 부분 역시 그려보면 쉬움.
                    acc[y][x] - acc[y - M][x] - acc[y][x - M] + acc[y - M][x - M],
                )

        print(f"#{tc} {max_result}")

    ##########

    return


# [Review]

# 2차원 누적합도 그림으로 그려보니 쉽게 이해할 수 있었다.

# 다만, 이 문제는 범위가 적어 하나하나 슬라이싱 sum하면서
# 브루트포스를 돌리는 게 더 편했을지도.


if __name__ == "__main__":
    main()
