'''
문제
뱀과 사다리 게임을 즐겨 하는 큐브러버는 어느 날 궁금한 점이 생겼다.

주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있을까?

게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다.
게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다.
보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다.
예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다.
만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다.
도착한 칸이 사다리면, 사다리를 타고 위로 올라간다.
뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.
즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고,
뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

입력
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다.
x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다.
u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다.
모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다.
항상 100번 칸에 도착할 수 있는 입력만 주어진다.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.

예제 입력 1 
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
예제 출력 1 
3
5를 굴려 6으로 이동한다.
6을 굴려 12로 이동한다. 이 곳은 98로 이동하는 사다리가 있기 때문에, 98로 이동한다.
2를 굴려 100으로 이동한다.
예제 입력 2 
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
예제 출력 2 
5
5를 굴려 6으로 이동하고, 사다리를 이용해 80으로 이동한다. 
6을 굴려 86으로
6을 또 굴려 92로
6을 또 굴려 98로 이동하고
2를 굴려 100으로 이동한다.
'''

# 그냥 개쉬운문제임.
# 그래프에 주사위굴려서 갈수있는칸 n + 1~6 저장하고
# 추가로 사다리만 넣어준다음에 bfs돌려서 100까지가면 끝나는거임.

# 풀다 보니 생기는 문제가 있다.
# 그래프 간선이 6개가 들어가니까 사다리가 없는경우 너무 오래걸린다.
# 6칸 내에 사다리가 없으면 그냥 무조건 6을 고정으로 뽑아도 될 듯.
'''
from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(101)]

# 사다리와 뱀의 경우, 앞 6칸에 간선을 추가한다.
# 사다리나 뱀이 시작되는 칸에는 간선을 추가하지 않는다.
for _ in range(N + M):
    X, Y = map(int, input().split())
    graph[X] = [0] # 사다리나 뱀이 시작되는 칸을 구분한다.
    for i in range(1, 7):
        if 0 < X - i and graph[X - i] != [0]:
            graph[X - i].append(Y)

# 주사위 범위에 사다리나 뱀이 없는 경우는 6만 넣고,
# 있다면 주사위에 뱀보다 큰 칸을 하나 추가해준다. (100에 도착하는 경우 제외)
# 뱀이 +6이면 하나 작은 칸을 추가해준다.
for i in range(1, 101):
    if graph[i] == [0]:
        continue
    elif graph[i]:
        for j in range(6, 0, -1):
            if i + j < 101:
                if graph[i + j] != [0]:
                    graph[i].append(i + j)
                    break
    else:
        for j in range(6, 0, -1):
            if i + j < 101:
                graph[i].append(i + j)
                break

# 주사위 횟수를 저장함과 동시에 중복 방문이 없도록 한다.
distance = [-1] * 101

# bfs를 돌려 최단거리를 찾는다.
def bfs():
    queue = deque()
    queue.append(1)
    distance[1] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                if neighbor == 100:
                    return

bfs()
print(distance[100])
'''
# 0 0의 경우 시간초과
# 뱀 시작칸 앞 6칸 내에서 사다리가 시작되는 경우
# 갈 칸이 한칸 빼고 다 뱀인 경우

# 여러가지 시행착오를 거쳐 맞긴 했는데, 그리디를 안쓰고는 못 풀까.

from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

portal = [0] * 101
for _ in range(N + M):
    A, B = map(int, input().split())
    portal[A] = B

distance = [-1] * 101
def bfs():
    queue = deque()
    queue.append(1)
    distance[1] = 0

    while queue:
        current = queue.popleft()
        if current == 100:
            return

        if portal[current] != 0:
            # 01bfs를 이용한다.
            # 점프를 뛰는 경우가 무조건 최단거리임. 우선되어야함
            queue.appendleft(portal[current])
            distance[portal[current]] = distance[current]
        else:
            for dice in range(1, 7):
                if current + dice <= 100 and distance[current + dice] == -1:
                    queue.append(current + dice)
                    distance[current + dice] = distance[current] + 1

bfs()
print(distance[100])

'''
01bfs안쓰면 틀리는 케이스
사다리, 뱀, 사다리로 가는게 빠른경우
2 3
29 87
7 41
81 30
52 31
47 27
'''