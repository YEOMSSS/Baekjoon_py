# 브루트포스로 0인 칸을 전부 조합을 돌려서
# 모든 경우에 벽을 세워보면 되겠다.

# 그리고 안전지대를 세야하는데.. 이건 bfs로 하면 되겠지.
# 벽을 만날 때까지 돌려서 바이러스를 만나지 않았다면 칸의 수를 전부 누적하자.

# 아니야, 2로 가득 채운 다음에 남아있는 0의 개수를 세면 되지.

from collections import deque
from itertools import combinations

N, M = map(int, input().split())

maps_default = [list(map(int, input().split())) for _ in range(N)]

# 입력된 지도에서 바이러스, 빈 칸 좌표 찾기
viruses = []
not_walls = []
for row in range(N):
    for col in range(M):
        current = maps_default[row][col]
        if current == 0:
            not_walls.append(row * M  + col)
        if current == 2:
            viruses.append(row * M + col)

# 상하좌우 dx dy
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 브루트포스로 벽을 세우는 모든 경우 찾기
new_wall_locates = combinations(not_walls, 3)

def bfs(comb, maps_default):
    # 방문 확인 배열
    visited = [False] * (N * M)
    
    # 3개의 벽을 새로 세우기
    for coord in comb:
        maps_default[coord // M][coord % M] = 1
        
    # 큐 만들기
    queue = deque()
    # 시작 바이러스 큐에 push
    for virus in viruses:
        queue.append(virus)
        visited[virus] = True

    while queue:
        current = queue.popleft()
        row = current // M
        col = current % M

        # current마다 상하좌우 반복
        for dx, dy in directions:
            row_next = row + dx
            col_next = col + dy
            current_next = row_next * M + col_next
            # 다음 좌표가 미방문이며 빈 칸일 경우 push
            if 0 <= row_next < N and 0 <= col_next < M and not visited[current_next]:
                if maps_default[row_next][col_next] == 0:
                    queue.append(current_next)
                    visited[current_next] = True

    # 안전구역 찾기. 미방문된 빈칸은 안전구역이다.
    safe_zone = 0
    for idx, check in enumerate(visited):
        if not check and maps_default[idx // M][idx % M] == 0:
            safe_zone += 1

    # 세웠던 벽을 다시 제거해서 원상복귀
    for coord in comb:
        maps_default[coord // M][coord % M] = 0
    
    return safe_zone

# 벽을 새로 세운 모든 조합에 대하여 bfs를 돌려 최댓값 찾기
result = 0
for wall_comb in new_wall_locates:
    result = max(result, bfs(wall_comb, maps_default))

print(result)

# 원콤. 내일 주석 써보자.