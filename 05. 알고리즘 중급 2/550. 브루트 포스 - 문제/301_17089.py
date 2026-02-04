# Authored by : marigold2003
# Date : 2026-02-04
# Link : https://www.acmicpc.net/problem/17089

import sys

input = sys.stdin.readline


# [Summary]

# N명의 사람이 있고, 이 중 서로 친구인 셋을 고른다.
# 세 사람의 친구의 합의 최솟값을 구하시오.


def main():

    # [Ideas]

    # 그래프를 set으로 만들어보자.

    # 모든 간선(친구관계)에 대해서 세 번째 친구를 확인한다.
    # 한 친구의 친구가 다른 친구의 친구인지를 in으로 확인하면 될 듯.
    # 굳이 사이클까지 볼 것도 없구만.

    ##########

    N, M = map(int, input().split())

    graph = [set() for _ in range(N + 1)]
    friend_count = [0] * (N + 1)

    queue = []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
        friend_count[a] += 1
        friend_count[b] += 1

        # 순서를 강제하여 12, 13, 23으로 들어가게 한다.
        # 21, 31, 32의 경우가 사라져 절반으로 줄어듬
        if a < b:
            queue.append((a, b))
        else:
            queue.append((b, a))

    answer = sys.maxsize

    # 모든 간선에서 제3의 친구 c를 탐색
    for a, b in queue:
        # 차수가 더 작은 set을 순회하여 연산 횟수 최적화
        target, other = (a, b) if friend_count[a] < friend_count[b] else (b, a)

        for c in graph[target]:
            # c가 b일때만 확인하여 오름차순 삼각형만 검사, 13, 23의 경우가 사라져 1/3으로 줄어듬
            if c > b and c in graph[other]:
                answer = min(
                    answer, friend_count[a] + friend_count[b] + friend_count[c] - 6
                )

    print(answer if answer != sys.maxsize else -1)

    ##########

    return


# [Review]

# 역시 최적화는 중요하다.
# 게을리 하지 말자.


if __name__ == "__main__":
    # wrong()
    main()


def wrong() -> None:

    # [Ideas]

    # 친구인 셋을 찾기만 하면 쉽다.
    # 어? 이거 사이클인가? 3번 이동해서 원래로 돌아오게 되면 성공.
    # 음, 세칸 이동했는데 세칸 전과 같다면 성공?

    # 음, 굳이 사이클을 사용하지 말아볼까.

    # 최적화를 더 할 수 있을 것이다. 중복을 제거하지 않는 코드다.
    # 6배 비효율적인 코드임. 역시 메모리 초과가 나는가

    ##########

    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    friend_count = list(map(len, graph))

    from collections import deque

    result = sys.maxsize

    def bfs(start):
        nonlocal result
        queue = deque()

        queue.append(([start], 0))

        while queue:
            curr, moves = queue.popleft()

            if moves == 3:
                if curr[-1] == start:
                    result = min(result, sum(friend_count[i] for i in curr[:-1]) - 6)
                continue

            for nei in graph[curr[-1]]:
                if moves >= 2 and nei == curr[-2]:
                    continue
                queue.append((curr + [nei], moves + 1))

    for i in range(1, N + 1):
        bfs(i)

    print(result if not result == sys.maxsize else -1)

    ##########

    return
