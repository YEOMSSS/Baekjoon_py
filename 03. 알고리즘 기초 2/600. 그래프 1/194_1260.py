'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
'''
# 드디어 그래프까지 왔다
# 최대 한계로 살고 싶어

import sys
input = sys.stdin.readline

from collections import deque

# 노드개수, 간선개수, 시작노드번호
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for row in graph: # 오름차로 정렬
    row.sort()

def dfs(start):
    stack = [start]
    visited = set()
    visit_order = [] # 순서 저장용

    while stack:
        node = stack.pop()
        if node in visited:
            continue        
        visited.add(node)
        visit_order.append(node)

        for nei in reversed(graph[node]): # 내림차로 넣어야 탐색을 오름차로함
            if nei not in visited:
                stack.append(nei)
    
    print(*visit_order)

'''
# 재귀 DFS
def dfs(node, visited, visit_order):
    if node in visited:
        return
    visited.add(node)
    visit_order.append(node)

    for neighbor in graph[node]:  # 오름차순 탐색
        dfs(neighbor, visited, visit_order)

# 실행
visited = set()
visit_order = []
dfs(V, visited, visit_order)
print(*visit_order)
'''

def bfs(start):
    queue = deque([start])
    visited = set()
    visit_order = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        visit_order.append(node)

        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)

    print(*visit_order)

dfs(V)
bfs(V)