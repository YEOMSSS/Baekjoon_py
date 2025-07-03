'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때,
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
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

def bfs(node, destination):
    if node == destination:
        return 0
    queue = deque()
    queue.append(node)
    distance[node] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                if neighbor == destination:
                    return distance[current] + 1 # 현재에서 1초 지나면 도착 가능
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

print(bfs(N, K))
