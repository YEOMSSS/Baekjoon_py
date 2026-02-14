# Authored by : marigold2003
# Date : 2026-02-14
# Link : https://www.acmicpc.net/problem/4902


import sys

input = sys.stdin.readline


# [Summary] 삼각형의 값

# 삼각형이 있다.
# 길이가 1인 단위삼각형으로 이루여져 있으며, 높이는 최대 400이다.
# 단위삼각형의 값은 그 안에 쓰여 있는 값이 되며, 부분삼각형의 값은 그 안에 있는 단위삼각형의 값의 합이 된다.
# 삼각형의 모든 부분삼각형 중 가장 큰 값을 갖는 부분삼각형의 값을 구하여라.


def main() -> None:

    # [Ideas]

    # 일단 브루트포스긴 하다.
    # 모든 부분삼각형을 확인해야 한다는 건 변하지 않는다.
    # 음수가 섞여 있기 때문에 진짜 전부 확인해야 한다. 양수뿐이면 무조건 제일 큰거겠지

    # 그런데 부분삼각형의 값을 구할 때마다 덧셈연산을 해서는 답이 없다.
    # 누적합을 이용해야 한다. 어차피 연속된 부분으로 이루어져 있으니까

    # 부분삼각형의 값을 구할 때는 슬라이싱 느낌이 될 것이기 때문에, 이걸 누적합으로 퉁칠 수 있을 듯.
    # 1줄은 0:1, 2줄은 0:3, 3줄은 0:5...이런식으로 더해지니까 규칙성도 있음
    # 오른쪽으로 갈 대는 뒤집힌건 건너뛰니까 2:3, 2:5... 이렇게 된다.

    # 입력받은 값까지의 합을 계속 넣어주면서 만들면 될 듯.
    # 아, 삼각형이 뒤집혀 있을 수도 있다.

    ##########

    testcase = 0
    while True:
        testcase += 1

        nums_input = tuple(map(int, input().split()))
        N = nums_input[0]
        if not N:
            return

        # N줄에 대한 삼각형 누적합 배열 만들기
        prefix_sum = [[0] for _ in range(N)]

        curr_sum = 1
        for r in range(N):
            for n in nums_input[curr_sum : curr_sum + r * 2 + 1]:
                prefix_sum[r].append(n + prefix_sum[r][-1])
            curr_sum += r * 2 + 1

        # 부분삼각형 탐색 시작

        answer = -sys.maxsize

        # 삼각형 시작위치 찾기
        for r in range(N):
            # 정방향 부분삼각형의 시작열
            for c in range(1, r * 2 + 2, 2):

                # 시작점에서 만들 수 있는 정방향 부분삼각형 전부 찾기
                curr_sum = 0
                for size in range(N - r):
                    curr_sum += (
                        prefix_sum[r + size][c + size * 2] - prefix_sum[r + size][c - 1]
                    )
                    answer = max(answer, curr_sum)

            # 역방향은??
            for c in range(2, r * 2 + 2, 2):
                curr_sum = 0
                # 열 확인, 행 확인 후 더 작은 것으로 크기 설정
                for size in range(min(c // 2, r - c // 2 + 1)):
                    curr_sum += (
                        prefix_sum[r - size][c] - prefix_sum[r - size][c - size * 2 - 1]
                    )
                    answer = max(answer, curr_sum)

        print(f"{testcase}. {answer}")

    ##########

    return


# [Review]

# 400줄이 이걸로 가능할지...
# 쌉가능이다. pypy로만 제출 가능한 문제였다.
# 역시 종이에 직접 그림 그리면서 푸는게 인덱스 오류가 없다.

# 아 기분좋아라.


if __name__ == "__main__":
    main()
