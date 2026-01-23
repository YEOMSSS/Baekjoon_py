import sys

input = sys.stdin.readline

from collections import deque


# 목표중량으로 start->end 이동가능한지 확인
def bfs(graph, start, end, target_weight) -> bool:

    queue = deque()
    visited = [False] * (len(graph) + 1)

    queue.append(start)
    visited[start] = True

    while queue:
        curr = queue.popleft()

        if curr == end:
            return True

        for nei, nei_weight in graph[curr]:
            if visited[nei]:
                continue
            if nei_weight < target_weight:
                continue
            queue.append(nei)
            visited[nei] = True

    return False


# 이분탐색을 이용해 start->end 이동가능한 최대중량 찾기
def b_search(graph, start, end):
    left = 0
    right = 1_000_000_000  # 최대 중량

    result = 0

    while left <= right:
        mid = (left + right) // 2

        # 도착할 수 있다면 중량을 늘려봐도 된다.
        if bfs(graph, start, end, mid):
            result = mid
            left = mid + 1
        # 도착할 수 없다면 중량을 줄여야만 한다.
        else:
            right = mid - 1

    return result


def main() -> None:
    # 섬 개수, 다리 개수
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        # a섬과 b섬 사이에 중량제한이 c인 다리 건설
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 시작섬, 도착섬
    start, end = map(int, input().split())

    print(b_search(graph, start, end))


if __name__ == "__main__":
    main()
