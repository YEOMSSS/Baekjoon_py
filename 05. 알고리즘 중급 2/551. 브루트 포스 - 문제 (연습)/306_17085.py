# Authored by : marigold2003
# Date : 2026-02-10
# Link : https://www.acmicpc.net/problem/17085


import sys

input = sys.stdin.readline


# [Summary] 제목

# 가로세로 길이가 같은 십자가가 다양하게 있다.
# 보드가 있는데, 이 위에 십자가를 두 개 올려놓을 것이다.
# "#"표시된 부분에만 십자가를 놓을 수 있다.
# 십자가의 넓이의 곱이 가장 크게 해라.


def main() -> None:

    # [Ideas]

    # 289_16924번의 십자가 생성 방식을 그대로 가져오자.
    # 점을 2개 골라서 두 점에서 각각 십자가를 가장 크게 만들어야 한다.
    # 15*15보드에서 점 225개, 점 2개 선택하는 경우의 수 225*224//2 = 25200번. 브루트포스 가능

    # 문제는 두 십자가가 겹칠 때다.
    # 넓이의 곱이 최대가 되려면 하나만 크고 하나는 작은 건 안 된다.
    # 두 십자가의 크기를 둘 다 최대한으로 키워야 한다.

    # 두 점을 선택하고, 1번점에서 최대 십자가 후 2번점 최대 십자가
    # 2번점에서 최대 십자가 후 1번점에서 최대 십자가. 이렇게 2회 비교해야겠다.

    # 그래도 비교가 50400번이니까 충분히 가능할듯
    # 이럴거면 그냥 순열로 전부 검사하면 되잖아? 에라이

    # 그런데, 둘을 동시에 키워야 하는 경우가 생길 수밖에 없다.
    # 두 점에서 동시에 한 칸씩 키우다가 겹칠 때
    # 그때 둘로 갈라야 할 듯.

    ##########

    from itertools import permutations

    N, M = map(int, input().split())

    # 인덱스 처리 귀찮으니 padding을 하자.
    board = (
        [["."] * (M + 2)]
        + list(["."] + list(input().rstrip()) + ["."] for _ in range(N))
        + [["."] * (M + 2)]
    )

    can_use = set()
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if board[r][c] == "#":
                can_use.add((r, c))

    # r, c에서 만들 수 있는 가장 큰 십자가가 차지하는 좌표들을 반환
    def check(r_a, c_a, r_b, c_b) -> set:

        route_a = set()
        route_b = set()

        route_a.add((r_a, c_a))
        route_b.add((r_b, c_b))

        d = 1

        flag_a = True
        flag_b = True

        while True:

            if flag_a:
                for dr, dc in ((0, -d), (0, d), (-d, 0), (d, 0)):
                    nr, nc = r_a + dr, c_a + dc
                    if (nr, nc) in route_b or board[nr][nc] == ".":
                        flag_a = False
                        break

            if flag_b:
                for dr, dc in ((0, -d), (0, d), (-d, 0), (d, 0)):
                    nr, nc = r_b + dr, c_b + dc
                    if (nr, nc) in route_a or board[nr][nc] == ".":
                        flag_b = False
                        break

            if flag_a and flag_b:
                temp = set(
                    (
                        (r_a, c_a - d),
                        (r_a, c_a + d),
                        (r_a - d, c_a),
                        (r_a + d, c_a),
                        (r_b, c_b - d),
                        (r_b, c_b + d),
                        (r_b - d, c_b),
                        (r_b + d, c_b),
                    )
                )
                # 두 십자가의 확장이 겹치는 경우 a만 계속 진행한다.
                if len(temp) != 8:
                    flag_b = False

            if flag_a:
                route_a.update(
                    [(r_a, c_a - d), (r_a, c_a + d), (r_a - d, c_a), (r_a + d, c_a)]
                )

            if flag_b:
                route_b.update(
                    [(r_b, c_b - d), (r_b, c_b + d), (r_b - d, c_b), (r_b + d, c_b)]
                )

            if flag_a or flag_b:
                d += 1
                continue

            break

        return len(route_a) * len(route_b)

    answer = 0
    for a, b in permutations(can_use, 2):
        r_a, c_a = a
        r_b, c_b = b

        answer = max(answer, check(r_a, c_a, r_b, c_b))

    print(answer)

    ##########

    return


# [Review]

# 브루트포스로 푼다는 발상을 하는 게 생각만큼 쉽지는 않을지도.
# 구현도 아주 막 간단한 것만은 아니다.
# 아니, 생각보다 쉽지 않았다. 꽤나 어렵다...


if __name__ == "__main__":
    main()
