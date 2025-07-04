'''
입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17
'''
# 최단거리네. 간선을 어떻게 연결해야 할까?
# 그래프가 단방향이다. 2*x의 위치로 이동할 땐.

from collections import deque

N, K = map(int, input().split())

# 점 100000에 있으면 200000까지 갈 수 있다?
# 아니, 모든 경우에서 100000이면 충분하다. 왠진몰라. 통과되네.
graph = [set() for _ in range(100_001)]

for i in range(100_000):
    # 앞이나 뒤로 가는 경우
    graph[i].add(i + 1)
    graph[i + 1].add(i)
    # 두배로 가는 경우
    if i <= 50_000: # 2*i <= 100000
        graph[i].add(2 * i)

distance = [-1] * 100001
parents = [None] * 100001

def bfs(node, destination):
    queue = deque()
    queue.append(node)
    distance[node] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                if neighbor == destination:
                    distance[destination] = distance[current] + 1 # 목적지노드에 거리추가해주고
                    parents[destination] = current # 목적지노드의 부모추가해주고
                    return
                distance[neighbor] = distance[current] + 1
                parents[neighbor] = current # 현시점에서의 부모노드를 갱신해줌
                queue.append(neighbor)

bfs(N, K)

# 똑같은게 들어올때를 고려
if N == K:
    print(0)
    print(K)
else:
    print(distance[K])

    # 최단거리상태의 부모노드 리스트를 이용해
    # 거꾸로 그래프를 타고 올라간다.
    answer = deque()
    node = K
    while node != N:
        answer.appendleft(node)
        node = parents[node]
    answer.appendleft(N)
    print(*answer)