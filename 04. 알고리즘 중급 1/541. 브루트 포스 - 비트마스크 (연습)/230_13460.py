'''
문제
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다.
가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다.
게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다.
빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다.
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
'.'은 빈 칸을 의미하고,
'#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치,
'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다.
구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다.
만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

예제 입력 6 
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########
예제 출력 6 
7
예제 입력 7 
3 10
##########
#.O....RB#
##########
예제 출력 7 
-1
'''

# 뭔가 익숙한 문제인데?
# 그래프로 만들어서 풀었던 것 같다. 몇 번이더라?
# 그래. 531.222_16197. 동전 하나만 떨구기.
# 그런데 다른 점은 한칸씩 이동이 아니라 그냥 주르륵 떨어지는거네. 어려운데?
        
# 좌표마다 상하좌우로 떨구면 어디에 떨궈지는지를 저장하자.
# 벽을 만날때까지 한칸 지날때마다 카운트해서 그 값으로 좌표를 갱신해서 저장하자.
# 카운트 0이면 그냥 원래 위치 그대로.

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]

# 한칸짜리 보드일 경우 즉시 종료. 불가능한 경우
# 근데 필요 없잖아 이거. 문제 조건에 이미 빠졌는데
# if N == M == 1:
#     print(-1)
#     exit()


# 상하좌우에 맞춰 벽에 닿을 때까지 반복해서 닿는 위치의 좌표를 찾는다.
# 만약 바로 벽을 만나면 갱신 없음.
def graph_maker(row, col, direction, prev):
    if maps[row][col] == "#":
        return prev
    elif maps[row][col] == "O":
        return -7
    else:
        prev = row * M + col
        if direction == 0:
            return graph_maker(row - 1, col, direction, prev)
        elif direction == 1:
            return graph_maker(row + 1, col, direction, prev)
        elif direction == 2:
            return graph_maker(row, col - 1, direction, prev)
        elif direction == 3:
            return graph_maker(row, col + 1, direction, prev)

# 상하좌우로 기울일 때 구슬이 이동하는 위치를 좌표마다 저장한다.
graph = [[-1] * 4 for _ in range(N * M)]
red_ball_coord = 0
blue_ball_coord = 0

for row in range(N):
    for col in range(M):
        current_coord = maps[row][col]

        # 벽일 때는 아예 확인할 필요가 없다.
        if current_coord == "#":
            continue

        else:
            current = row * M + col
            if current_coord == "R":
                red_ball_coord = current
            elif current_coord == "B":
                blue_ball_coord = current

            # 어차피 벽으로 둘러싸여 있으니 인덱스 넘을 일 없음.
            # 현 위치에서 상하좌우로 기울일 때 어디로 구슬이 이동하는지 저장.
            for direction in range(4):
                graph[current][direction] = graph_maker(row, col, direction, current)


def bfs():
    queue = deque()
    visited = set()

    # 빨강, 파랑, 기울인횟수로 묶어서 큐에 밀어넣기
    queue.append((red_ball_coord, blue_ball_coord, 0))

    while queue:
        current = queue.popleft()
        red, blue, count = current

        # 중복되는 동전위치가 온 경우 스킵
        if (red, blue) not in visited:
            visited.add((red_ball_coord, blue_ball_coord))

            # 버튼 최대 횟수 10회 확인, 11회 누르자마자 종료
            if count == 11:
                print(-1)
                return
            
            # 정답 조건 확인. 빨간 구슬만 떨어지면 바로 종료
            if red == -7:
                print(count)
                return
            
            for direction in range(4):
                next_red, next_blue = graph[red][direction], graph[blue][direction]

                # 구슬이 겹치는 경우 해결. (둘다 구멍에 위치한 경우 제외)
                # 위로 밀 때는 더 밑에있던 구슬이 한 칸 내려간다.
                # 아래로 밀 때는 더 위에있던 구슬이 한 칸 올라간다.
                # 좌로 밀 때는 더 우에있던 구슬이 한 칸 우로간다.
                # 우로 밀 때는 더 좌에있던 구슬이 한 칸 좌로간다.
                if next_red == next_blue != -7:
                    if direction == 0:
                        if red < blue:
                            next_blue += M
                        else:
                            next_red += M
                    elif direction == 1:
                        if red < blue:
                            next_red -= M
                        else:
                            next_blue -= M
                    elif direction == 2:
                        if red < blue:
                            next_blue += 1
                        else:
                            next_red += 1
                    elif direction == 3:
                        if red < blue:
                            next_red -= 1
                        else:
                            next_blue -= 1

                # 파란 구슬이 떨어지면 인정되지 않음
                if not next_blue == -7:
                    queue.append((next_red, next_blue, count + 1))
    print(-1)

# 실행
bfs()
    
'''
3 5
#####
#ORB#
#####
1
'''

# 풀었다 씨바아아알