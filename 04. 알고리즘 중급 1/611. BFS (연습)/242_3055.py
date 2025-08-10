'''
문제
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다.
이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 
비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽)
물도 매 분마다 비어있는 칸으로 확장한다.
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다.
물과 고슴도치는 돌을 통과할 수 없다.
또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다.
즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다.
이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다.
만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.

예제 입력 1 
3 3
D.*
...
.S.
예제 출력 1 
3
예제 입력 2 
3 3
D.*
...
..S
예제 출력 2 
KAKTUS
예제 입력 3 
3 6
D...*.
.X.X..
....S.
예제 출력 3 
6
예제 입력 4 
5 4
.D.*
....
..X.
S.*.
....
예제 출력 4 
4
'''

# 이동가능한 칸을 visited=False로 만들어두자.
# 전체를 False로 두고, 물을 True로 만들어주자.
# 그리고 한번 턴이 지날 때마다 물이 번진 칸들을 True로 만들자.

# 물이 번지는 걸 따로 만들어주자. 돌이랑 굴은 물이 못 간다.

import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, destination):
    destination_x = destination[0]
    destination_y = destination[1]

    # 이동하는 칸이 들어오는 큐, 시작 좌표 push
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    # 물이 퍼지는 큐를 따로 제작, 시작 물 좌표 push
    water_queue = deque()
    for coord in water_coords:
        water_queue.append(coord)
        water_visited[coord[0]][coord[1]] = True

    # 현재 이동에 걸린 시간
    current_distance = 0

    while queue:
        # 물을 미리 퍼트려 둬야 이동불가한 칸을 확인 가능
        for _ in range(len(water_queue)):
            x, y = water_queue.popleft()

            # 4방향에 대해 조건에 맞춰 물 퍼트리기
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 인덱스 초과, 돌일 때, 굴일 때, 이미 물일 때 제외
                if nx < 0 or R <= nx or ny < 0 or C <= ny:
                    continue
                if rock[nx][ny]:
                    continue
                if nx == destination_x and ny == destination_y:
                    continue
                if water_visited[nx][ny]:
                    continue

                water_queue.append((nx, ny))
                water_visited[nx][ny] = True

        for _ in range(len(queue)):
            x, y = queue.popleft()

            # 굴에 도달 시 조건 만족, 즉시 종료
            if x == destination_x and y == destination_y:
                print(current_distance)
                return

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 인덱스 초과, 물일 때, 돌일 때, 이미 방문했을 때 제외
                if nx < 0 or R <= nx or ny < 0 or C <= ny:
                    continue
                if water_visited[nx][ny]:
                    continue
                if rock[nx][ny]:
                    continue
                if visited[nx][ny]:
                    continue

                queue.append((nx, ny))
                visited[nx][ny] = True

        # 거리 증가 (시간 증가)
        current_distance += 1

    # 큐 소진 시 종료
    print("KAKTUS")
    return

# 크기가 R*C인 티떱숲의 지도 입력받기
R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

# 돌 위치 저장, 물의 시작 좌표 저장
rock = [[False for _ in range(C)] for _ in range(R)]
water_coords = []

# 고슴도치, 비버집, 물 시작좌표 찾기
for x in range(R):
    for y in range(C):
        current = board[x][y]
        if current == "S":
            start_coord = (x, y)
        elif current == "D":
            destination_coord = (x, y)
        elif current == "*":
            water_coords.append((x, y))
        elif current == "X":
            rock[x][y] = True

# 상하좌우에 대한 변화량
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 방문 확인 배열, 물 확인 배열
visited = [[False for _ in range(C)] for _ in range(R)]
water_visited = [[False for _ in range(C)] for _ in range(R)]

bfs(start_coord, destination_coord)

# 잘 풀었다! 원콤