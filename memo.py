from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_cycle(start):
    stack = [start]
    visited = [False] * (N + 1)
    parent = [-1] * (N + 1)

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    parent[neighbor] = current
                    stack.append(neighbor)
                elif parent[current] != neighbor:
                    # 사이클 발견
                    cycle = []
                    x = current
                    while x != neighbor:
                        cycle.append(x)
                        x = parent[x]
                    cycle.append(neighbor)
                    return cycle
    return []

cycle_nodes = find_cycle(1)

# BFS로 사이클까지의 거리 계산
distance = [-1] * (N + 1)
queue = deque()

for node in cycle_nodes:
    queue.append(node)
    distance[node] = 0

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

print(" ".join(map(str, distance[1:])))
