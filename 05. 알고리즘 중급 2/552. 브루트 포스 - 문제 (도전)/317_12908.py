# Authored by : marigold2003
# Date : 2026-02-23
# Link : https://www.acmicpc.net/problem/12908


import sys

input = sys.stdin.readline


# [Summary] 텔레포트 3

# 텔포입구에서 텔포출구로 이동하는 텔포가 3개 주어진다.
# 상하좌우 1칸이동에 1초, 텔포에 10초 사용한다.
# 출발지에서 도착지로 이동하는 최단시간을 구하시오.


def main() -> None:

    # [Ideas]

    # 텔레포트 16958번보다 이걸 먼저 풀었어야겠는데;

    # 똑같다. 최단거리로 점프해서 그냥 이동하는것과
    # 텔레포트를 타는 경우를 전부 더하면 됨.
    # 다만 이번에는 텔레포트를 여러번 탈 수도 있다.

    # 텔레포트를 타는 경우의 수: 78가지 (텔포 거꾸로 포함)
    # 텔레포트 한개 타는경우 2*3 6가지
    # 텔레포트 두개 타는경우 2*2*6 24가지
    # 텔레포트 세개 타는경우 2*2*2*6 48가지

    # start jump 텔포입구 tp 텔포출구 jump 텔포입구 tp 텔포출구 jump goal
    # 아몰랑, 하드코딩하자.

    ##########

    from itertools import permutations

    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    teleports = []
    for _ in range(3):
        x1, y1, x2, y2 = map(int, input().split())
        teleports.append(((x1, y1), (x2, y2)))

    # 점프만으로 a에서 b로 이동하는 시간을 구하는 func
    def jump_time(a: list[int], b: list[int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # 일단 점프만으로 목적지까지 이동해보기
    answer = jump_time(start, goal)

    # 텔레포트 한개 타는 경우
    for tp_in, tp_out in teleports:

        answer = min(answer, jump_time(start, tp_in) + 10 + jump_time(tp_out, goal))
        answer = min(answer, jump_time(start, tp_out) + 10 + jump_time(tp_in, goal))

    # 텔레포트 두개 타는 경우
    for tp_a, tp_b in permutations(teleports, 2):

        for a_in, a_out in (tp_a, tp_a[::-1]):
            for b_in, b_out in (tp_b, tp_b[::-1]):
                result = (
                    jump_time(start, a_in)
                    + 10
                    + jump_time(a_out, b_in)
                    + 10
                    + jump_time(b_out, goal)
                )
                answer = min(answer, result)

    # 텔레포트 세개 타는 경우
    for tp_a, tp_b, tp_c in permutations(teleports, 3):

        for a_in, a_out in (tp_a, tp_a[::-1]):
            for b_in, b_out in (tp_b, tp_b[::-1]):
                for c_in, c_out in (tp_c, tp_c[::-1]):
                    result = (
                        jump_time(start, a_in)
                        + 10
                        + jump_time(a_out, b_in)
                        + 10
                        + jump_time(b_out, c_in)
                        + 10
                        + jump_time(c_out, goal)
                    )
                    answer = min(answer, result)

    print(answer)

    ##########

    return


# [Review]

# 최적화할수 있겠지만, 할게 적으니까 그냥 하자.
# 가끔은 타자연습도 필요해.


if __name__ == "__main__":
    main()
