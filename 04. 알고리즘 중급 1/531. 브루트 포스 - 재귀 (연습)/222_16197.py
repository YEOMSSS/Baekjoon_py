'''
문제
N×M 크기의 보드와 4개의 버튼으로 이루어진 게임이 있다.
보드는 1×1크기의 정사각형 칸으로 나누어져 있고, 각각의 칸은 비어있거나, 벽이다.
두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.

버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다.
버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동하게 된다.

동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 20)

둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.

o: 동전
.: 빈 칸
#: 벽
동전의 개수는 항상 2개이다.

출력
첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다.
만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.

예제 입력 1 
1 2
oo
예제 출력 1 
1
예제 입력 2 
6 2
.#
.#
.#
o#
o#
##
예제 출력 2 
4
예제 입력 3 
6 2
..
..
..
o#
o#
##
예제 출력 3 
3
예제 입력 4 
5 3
###
.o.
###
.o.
###
예제 출력 4 
-1
예제 입력 5 
5 3
###
.o.
#.#
.o.
###
예제 출력 5 
3
'''

# 이동가능한 경로를 간선으로 저장해두고
# 순열로 상하좌우를 만들어서
# 10번까지 방향키 누를수있게하고
# 이동가능하면 위치옮기고 이동불가하면 그대로두기
# 그러고 모든 순열에 대해 하나만 떨어지는 최솟값 구하고
# 둘다떨어지거나 떨굴수없으면 -1

# 상0 하1 좌2 우3
# bfs를 해보자.
# -7, -7이면 이전걸로 되돌리고 계속
# 둘중 하나만 -7이면 depth 출력하고 바로 종료
# 거리를 누적해야 해서 중복제거는 어려울 듯
# 동전이 겹쳐지면 하나만 제거하는게 불가능해지니 어차피 걸러질듯

# 중복을 set()으로 처리해보자.
# 중복처리를 해주는게 훨씬 훨씬 빨리 돌아간다. 훠어어어얼씬

from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]

# 한칸짜리 보드일 경우 즉시 종료. 불가능한 경우
if N == M == 1:
    print(-1)
    exit()

# 그래프에 상하좌우 이동경로를 저장
graph = [[-1] * 4 for _ in range(N * M)]
coin_locate = []
for row in range(N):
    for col in range(M):
        current_locate = maps[row][col]

        # 벽 확인
        if current_locate == "#":
            continue
        # 벽이 아닐 경우 경로 저장
        else:
            current = row * M + col

            # 탈출가능여부 확인 (가능시 -7)
            if row == 0:
                graph[current][0] = -7
            if row == N - 1:
                graph[current][1] = -7
            if col == 0:
                graph[current][2] = -7
            if col == M - 1:
                graph[current][3] = -7

            # 동전 시작 위치 확인
            if current_locate == "o":
                coin_locate.append(current)

            # 우측 확인 후 양방향 경로 저장
            if col + 1 < M:
                right = current + 1
                if maps[row][col + 1] != "#":
                    graph[current][3] = right
                    graph[right][2] = current

            # 하단 확인 후 양방향 경로 저장
            if row + 1 < N:
                down = current + M
                if maps[row + 1][col] != "#":
                    graph[current][1] = down
                    graph[down][0] = current

# 동전 시작 위치 분리
default_coin1, default_coin2 = coin_locate

# 최단거리 찾기
def bfs():
    queue = deque()

    # 중복 확인용 set()
    visited = set()

    # 코인1위치, 코인2위치, 현재 버튼누른 횟수로 묶어 append
    queue.append((default_coin1, default_coin2, 0))

    while queue:
        current = queue.popleft()
        coin1, coin2, distance = current

        # 중복되는 동전위치가 온 경우 스킵
        if (coin1, coin2) in visited:
            continue
        else:
            visited.add((coin1, coin2))

        # 버튼 최대 횟수 10회 확인, 11회 누르자마자 종료
        if distance == 11:
            print(-1)
            return        
        
        # 정답 조건 확인, 동전이 하나만 떨어지면 바로 종료
        if coin1 == -7 or coin2 == -7:
            print(current[-1]) # distance만 print
            return
        
        # 상하좌우(0123)로 이동했을 때를 전부 집어넣기
        for i in range(4):
            next_coin1, next_coin2 = graph[coin1][i], graph[coin2][i]

            # 벽을 만나면 갱신 없음
            if next_coin1 == -1:
                next_coin1 = coin1                
            if next_coin2 == -1:
                next_coin2 = coin2

            # 둘 다 떨어지면 append 안함 (-7, -7)
            # 또는 동전이 같은 위치로 겹치면 append 안함.
            if not next_coin1 == next_coin2 == -7 or next_coin1 != next_coin2:
                queue.append((next_coin1, next_coin2, distance + 1))

    # 전부 중복되는 반복이나 벽에 박기,
    # 둘다 떨어지는 경우여서 깊이가 10을 채우지 못하는 경우
    print(-1)

# bfs 실행
bfs()

# 와, 졸라 잘푼듯??????