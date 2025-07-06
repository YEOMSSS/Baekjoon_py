'''
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다.
정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데,
하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고,
정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
각 줄의 마지막에는 -1이 입력으로 주어진다.
주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1 
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력 1 
11
'''
# 가중치가 있는 트리다.
# 루트에서 시작할 때 지름이 생기는 게 아니다.
# 1이 루트고 2,3이 자식이면 2와 3의 거리가 가장 멀다. 2-1-3 방문

import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())

# (자식, 가중치)로 graph[부모]에 저장되도록 해보자.
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0] # 가장 처음에 입력되는 노드 저장

    idx = 1
    while data[idx] != -1:
        neighbor = data[idx] # 입력된 이웃 노드 저장
        cost = data[idx + 1] # 입력된 이웃 노드와의 가중치 저장
        graph[node].append((neighbor, cost)) # 튜플형태로 (자식, 가중치) 저장
        idx += 2 # 인덱스 두칸 썼으니 두칸 옮기기

# 와, 이걸 어떻게 생각해내냐? dfs 두번써서 지름구하기라니..
# 일단 임의의 노드 하다 찝고 거기서 가장 먼 노드를 찾는다.
# 그리고 그 노드에서 가장 먼 노드를 찾아서 그 사이의 거리를 구한다...

# 가장 먼 노드를 찾는 dfsR
def dfsR(node, acc_cost, visited):
    visited[node] = True
    farthest = (node, acc_cost) # 현재 노드와 현재 누적 가중치

    for neighbor, cost in graph[node]:
        if not visited[neighbor]:
            result = dfsR(neighbor, acc_cost + cost, visited) # 간선의 가중치를 누적
            if result[-1] > farthest[-1]: # neighbor에서 리턴된 누적가중치가 현재보다 더 크면
                farthest = result # 갱신한다.
    # print(farthest)
    return farthest

# 임의 노드에서 가장 먼 노드 하나 찾아주기
visited = [False] * (V + 1)
far_node, _ = dfsR(1, 0, visited)

# 그 노드에서 가장 먼 노드와의 누적가중치 구하기(지름)
visited = [False] * (V + 1) # visited 초기화
_, diameter = dfsR(far_node, 0, visited)

print(diameter)