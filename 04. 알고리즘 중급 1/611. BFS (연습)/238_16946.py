'''
문제
N×M의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다.
두 칸이 변을 공유할 때, 인접하다고 한다.

각각의 벽에 대해서 다음을 구해보려고 한다.

벽을 부수고 이동할 수 있는 곳으로 변경한다.
그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다.

출력
맵의 형태로 정답을 출력한다.
원래 빈 칸인 곳은 0을 출력하고, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.

예제 입력 1 
3 3
101
010
101
예제 출력 1 
303
050
303
예제 입력 2 
4 5
11001
00111
01010
10101
예제 출력 2 
46003
00732
06040
50403
'''

# 쉬운데? 현재가 1인애들로 각각 bfs돌려서 바로 찍어내면 될듯.
'''
import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(coord):

    queue = deque()
    visited = [False] * (N * M)

    queue.append(coord)
    visited[coord] = True

    count_zero = 1

    while queue:
        current = queue.popleft()

        for dx, dy in directions:
            row = current // M + dx
            col = current % M + dy
            next_coord = row * M + col
            if 0 <= row < N and 0 <= col < M:
                if maps[row][col] == 0 and not visited[next_coord]:
                    visited[next_coord] = True
                    queue.append(next_coord)
                    count_zero += 1
    
    return count_zero % 10

result = ""
for coord in range(N * M):
    if maps[coord // M][coord % M] == 0:
        result += "0"
    else:
        result += str(bfs(coord))
    
for i in range(N):
    print(result[i * M : i * M + M])
'''

# 문제 잘읽어야지, %10을 해야한다.
# 시간초과? 아슬아슬하게 안되는거같은데, 뭘 줄여볼까?

# 아예 로직을 뒤집어야 할 것 같다.

# 0끼리 묶여있는 넓이를 구하고 인접한 벽에 넓이를 더해주자.
# 그러면 벽 하나마다 bfs 하지 않고 그냥 벽 묶음의 수만큼만 bfs를 하면 된다.

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(coord):
    queue = deque()
    visited = set()
    walls = set()

    queue.append(coord)
    visited.add(coord)

    count_zero = 1
    
    while queue:
        current = queue.popleft()

        for dx, dy in directions:
            row = current // M + dx
            col = current % M + dy
            next_coord = row * M + col
            if 0 <= row < N and 0 <= col < M and next_coord not in visited:
                if maps[row][col] == 0:
                    visited_zero.add(next_coord)
                    visited.add(next_coord)
                    queue.append(next_coord)
                    count_zero += 1
                elif maps[row][col] == 1 :
                    walls.add(next_coord)

    return count_zero % 10, walls

result = [0] * (M * N)
visited_zero = set()
for coord in range(M * N):
    row = coord // M
    col = coord % M
    if maps[row][col] == 0 and coord not in visited_zero:
        size, adjacent_walls = bfs(coord)
        for wall in adjacent_walls:
            result[wall] = (result[wall] + size) % 10
    if maps[row][col] == 1:
        result[coord] = (result[coord] + 1) % 10
    
for i in range(N):
    print("".join(map(str, (result[i * M : i * M + M]))))

# 음. 내일 아침에 주석을 달아보자.