'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
'''
# 간선이 들어오는데, 이거 클래스로 만들수 있는겨?
# dfs로 찾고, 어디에서 온건지를 저장해볼까?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 까먹지좀마.

N = int(input())

# 늘 하던 간선정보 넣어서 그래프 만들기
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 안하면 -1, 방문하면 부모노드를 저장
parents = [-1] * (N + 1)
# dfsR로 부모노드를 저장하는 트리 만들기
def build_tree(node, parent):
    parents[node] = parent

    for neighbor in graph[node]:
        if parents[neighbor] == -1:
            build_tree(neighbor, node)

# 루트는 1이고, 1의 부모노드는 없으니까 0으로
build_tree(1, 0)

print("\n".join(map(str, parents[2:])))