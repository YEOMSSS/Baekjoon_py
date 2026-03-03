# Authored by : marigold2003
# Date : 2026-03-03
# Link : https://www.acmicpc.net/problem/5014


import sys

input = sys.stdin.readline


# [Summary] 스타트링크

# F(1M)길이 수직선의 좌표 S에서 두 행동으로 G에 도착해야 한다.
# U만큼 더하기, D만큼 빼기.

# S에서 G로 이동하기 위해 필요한 행동의 최소 횟수를 구하시오.
# 불가능한 경우 use the stairs를 출력할 것

# 지하나 옥상은 갈 수 없다는 게 포인트다.


def main() -> None:

    # [Ideas]

    # 이거 수학으로 가능할까?
    # 그니까, bfs로 풀어지는건 알겠어, 알겠는데
    # 왜 bfs로 풀어야 하는건데?

    ##########

    F, S, G, U, D = map(int, input().split())

    from collections import deque

    queue = deque()
    visited = set()

    queue.append(S)
    visited.add(S)

    count = 0
    while queue:
        for _ in range(len(queue)):

            curr = queue.popleft()
            if curr == G:
                print(count)
                return

            nc = curr + U
            if nc <= F and nc not in visited:
                queue.append(nc)
                visited.add(nc)

            nc = curr - D
            if nc > 0 and nc not in visited:
                queue.append(nc)
                visited.add(nc)

        count += 1

    print("use the stairs")

    ##########

    return


# [Review]

# 빠른 bfs. 시간초과 문제는 없는가?
# 그리디로 아예 안되는거임 이거? 비스무리한 냄새는 좀 나는데.


if __name__ == "__main__":
    main()
