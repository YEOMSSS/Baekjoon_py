'''
문제
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다.
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다.
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다.
물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

출력
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
'''
'''
예제 입력 1 
3
0 0 0
0 0 0
0 9 0
예제 출력 1 
0
예제 입력 2 
3
0 0 1
0 0 0
0 9 0
예제 출력 2 
3
예제 입력 3 
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
예제 출력 3 
14
예제 입력 4 
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
예제 출력 4 
60
예제 입력 5 
6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
예제 출력 5 
48
예제 입력 6 
6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
예제 출력 6 
39
'''

# 시작사이즈는 2
# 작은거만 먹을 수 있음
# 같으면 이동만 가능
# 동일 시 우선순위는 위, 다음 우선순위는 좌
# 자신의 크기만큼 물고기를 먹으면 1 커진다
# 먹을 수 있는 물고기가 없는 순간 종료

# visited를 만들되, 물고기가 성장하면 초기화하자.

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
fish_board = [list(map(int, input().split())) for _ in range(N)]

# 물고기의 현재 위치9 찾기
fish_count = 0
for x in range(N):
    for y in range(N):
        current = fish_board[x][y]
        if current == 9:
            fish_x, fish_y = x, y
        elif current != 0:
            fish_count += 1

# 상좌우하에 대한 변화량
directions = ((-1, 0), (0, -1), (0, 1), (1, 0))

visited_fish = [[False for _ in range(N)] for _ in range(N)]

def bfs(start_x, start_y, fish, visited, board):
    # 처음부터 물고기가 없는 경우
    if fish == 0:
        print(0)
        return

    queue = deque()
    # x, y, status, current_eat
    queue.append([start_x, start_y, 2, 0])
    board[start_x][start_y] = 0
    visited_fish[start_x][start_y] = True

    current_distance = 0

    prev_distance = 0

    while queue:
        # 이동거리당으로 새 bfs가 실행되는 느낌
        fish_can_eat = []
        for _ in range(len(queue)):
            x, y, status, current_eat = queue.popleft()

            # 물고기를 다 먹어서 종료되는 경우
            if fish == 0:
                print(current_distance)
                return

            # 물고기 진화
            if status == current_eat:
                status += 1
                current_eat = 0

            # 더 먹을 수 있는 물고기가 없어서 종료되는 경우
            if all((value == 0) or (status <= value) for row in board for value in row):
                print(current_distance)
                return

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 인덱스 초과, 방문 시 제외, 더 큰 물고기를 만나면 제외
                if nx < 0 or N <= nx or ny < 0 or N <= ny:
                    continue
                if visited[nx][ny]:
                    continue
                if status < board[nx][ny]:
                    continue

                if board[nx][ny] == 0 or board[nx][ny] == status:
                    queue.append([nx, ny, status, current_eat])
                    visited[nx][ny] = True

                # 먹을 수 있는 물고기 찾기
                elif board[nx][ny] < status:
                    fish_can_eat.append((nx, ny))
                    visited[nx][ny] = True

        # 먹을 물고기를 고르고, 큐와 배열 초기화 (bfs를 새로 시작하는 느낌)
        if fish_can_eat:
            fish_can_eat.sort(key= lambda x: (x[0], x[1]))
            eat_x, eat_y = fish_can_eat[0]
            queue = deque()
            queue.append([eat_x, eat_y, status, current_eat + 1])
            visited = [[False for _ in range(N)] for _ in range(N)]
            visited[eat_x][eat_y] = True
            board[eat_x][eat_y] = 0
            fish -= 1

            prev_distance = current_distance + 1

        current_distance += 1

    # temp는 큐 소진시 초기화 전의 distance를 저장
    print(prev_distance)

bfs(fish_x, fish_y, fish_count, visited_fish, fish_board)


'''
3
0 0 1
9 0 4
2 3 1

3
2 4 1
9 2 3
0 2 0

'''
# 막힌 경우. 그냥 큐가 소진될 때랑 좀 다르다.. 큐 초기화 때문에.
# 그니까, 먹을 수 있는 물고기가 존재하긴 해도 그걸 먹지 못할 수 있다는 거다.
# 물고기를 먹은 후 visited이 초기화되니까 남은 빈칸을 다시 돌고 큐가 소진되어서 답이 다르게 나온다.