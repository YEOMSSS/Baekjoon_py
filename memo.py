# Authored by : marigold2003
# Date : 2026-02-04
# Link : https://www.acmicpc.net/problem/17089

import sys

input = sys.stdin.readline


# [Summary]

# N명의 사람이 있고, 이 중 서로 친구인 셋을 고른다.
# 세 사람의 친구의 합의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 친구인 셋을 찾기만 하면 쉽다.
    # 어? 이거 사이클인가? 3번 이동해서 원래로 돌아오게 되면 성공.

    # 음, 세칸 이동했는데 세칸 전과 같다면 성공?

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
                    print(curr, sum(friend_count[i] for i in curr[:-1]) - 6)
                    result = min(result, sum(friend_count[i] for i in curr[:-1]) - 6)
                continue

            for nei in graph[curr[-1]]:
                if moves >= 2 and nei == curr[-2]:
                    continue
                queue.append((curr + [nei], moves + 1))

    for i in range(1, N + 1):
        bfs(i)

    ##########

    return


# [Review]

#

if __name__ == "__main__":
    main()
