# Authored by : marigold2003
# Date : 2026-02-25
# Link : https://www.acmicpc.net/problem/16971


import sys

input = sys.stdin.readline


# [Summary] 배열 B의 값

# N(1000)*M(1000) arr A가 주어진다.
# 2*2 범위를 묶어 더해 (N-1)*(M-1) arr B를 만들 수 있다.
# A에서 임의의 두 row나 임의의 두 col의 위치를 교환할 수 있다.
# A에서 교환을 최대 1회 수행해 만들 수 있는 배열 B의 최댓값을 구하시오.


def brute() -> None:

    # [Ideas]

    # 교환은 bruteforce로 가능할 것으로 보인다.
    # 1000 * 999 // 2 = 499500 행열 두번이니까 999000회.

    # 999000회를 전부 확인해야 하는데, B를 999000회 만들 수는 없다.
    # B를 쉽게 만드는 법이 있을 것이다.

    # 그림으로 그려보니, 4개의 꼭짓점만 1회 더해지고
    # 모서리를 제외한 변은 2회 더해지며
    # 중앙부는 전부 4회 더해진다.

    # 이러면 999000회를 확인할 필요도 없지.
    # 중앙부끼리 바꾸는 건 합이 달라지지 않을 것이다.

    # 그렇다면, row [0]과 나머지를 바꾸거나 [N-1]과 나머지 바꾸기
    # col [0]과 나머지를 바꾸거니 [M-1]과 나머지 바꾸기
    # 대충 4000번만 확인하면 되는 것이다. 물론 양끝끼리도 바꿀필요 없다.

    # 이러면 B 구하기도 간단하다.
    # 각 row에 대한 122...221합 정보와 col에 대한 122...221정보를 저장해두자.
    # 그리고 모서리가 아닐 때만 *2해서 total로 사용하면 됨.
    # 직접 그려보는 건 역시 꽤나 중요하다.

    # 오, 다 *2상태로 더해둔 거에서 이번에 양끝으로 선택된 둘만 빼주는 식으로 가자.

    # 근데 풀다 보니 느낀건데, 이거 greedy다.
    # 양끝 둘중 큰거를 중앙에서 제일 작은거랑 바꾸면 되는거임.
    # 그걸 row랑 col에 대해서만 시도해주면 되는 간단한 문제였던 것이다...

    ##########

    N, M = map(int, input().split())

    board = list(list(map(int, input().split())) for _ in range(N))

    # row에 대해 교환해보기
    row_sum = list(map(lambda row: sum(row) * 2 - row[0] - row[-1], board))
    base_row = sum(row_sum) * 2

    # 교환이 없을 때로 시작하기
    answer = base_row - row_sum[0] - row_sum[-1]

    for i in range(1, N - 1):
        # row i를 row 0과 바꾸는 경우
        answer = max(answer, base_row - row_sum[-1] - row_sum[i])
        # row i를 row N-1과 바꾸는 경우
        answer = max(answer, base_row - row_sum[0] - row_sum[i])

    # col에 대해 교환해보기, zip(*board)로 col에 대한 list 사용
    col_sum = list(map(lambda col: sum(col) * 2 - col[0] - col[-1], zip(*board)))
    base_col = sum(col_sum) * 2

    for i in range(1, M - 1):
        # col i를 col 0과 바꾸는 경우
        answer = max(answer, base_col - col_sum[-1] - col_sum[i])
        # col i를 col M-1과 바꾸는 경우
        answer = max(answer, base_col - col_sum[0] - col_sum[i])

    print(answer)

    ##########

    return


def greedy() -> None:

    # [Ideas]

    # 근데 풀다 보니 느낀건데, 이거 greedy다.
    # 양끝 둘중 큰거를 중앙에서 제일 작은거랑 바꾸면 되는거임.
    # 그걸 row랑 col에 대해서만 시도해주면 되는 간단한 문제였던 것이다...

    # 양끝 row합중 큰거랑 나머지 row합중 작은거 교환
    # 양끝 col합중 큰거랑 나머지 col합중 작은거 교환
    # 교환없음. 이렇게 3개 비교하면 될 듯.

    ##########

    N, M = map(int, input().split())

    board = list(list(map(int, input().split())) for _ in range(N))

    # row에 대해 교환해보기
    row_sum = list(map(lambda row: sum(row) * 2 - row[0] - row[-1], board))
    base_row = sum(row_sum) * 2

    # 교환이 없을 때로 시작하기
    answer = base_row - row_sum[0] - row_sum[-1]

    # row가 2개뿐일 땐 바꿀 필요가 없다.
    if N != 2:

        # 양 끝 중 작은 것과 중간 중 작은 것이 새로운 양 끝이 된다.
        row_result = base_row - min(row_sum[-1], row_sum[0]) - min(row_sum[1:-1])
        answer = max(answer, row_result)

    # col이 2개뿐일 땐 바꿀 필요가 없다.
    if M != 2:

        # col에 대해 교환해보기, zip(*board)로 col에 대한 list 사용
        col_sum = list(map(lambda col: sum(col) * 2 - col[0] - col[-1], zip(*board)))
        base_col = sum(col_sum) * 2

        # 양 끝 중 작은 것과 중간 중 작은 것이 새로운 양 끝이 된다.
        col_result = base_col - min(col_sum[0], col_sum[-1]) - min(col_sum[1:-1])
        answer = max(answer, col_result)

    print(answer)

    ##########

    return


# [Review]

# 일단 bruteforce로 한번 풀었으니, greedy로도 해보자. 훨씬 빠를 것.
# greedy가 되니까 코드가 확 줄어든다.

# 근데 해놓고 보니 결국 누적합 잘 구해놓고 사칙연산 딸깍이라 비용적 측면에서 별 의미가 없네.

# 시간복잡도가 둘 다 O(N*M)이다. 누적합에 다 쓰니까.
# 오히려 greedy에서 슬라이싱하느라 더 잡아먹을수도 있다. 세상에.


if __name__ == "__main__":
    brute()
    # greedy()
