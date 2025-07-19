'''
문제
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

<그림 1>	<그림 2>	<그림 3>
<그림 1>의 경우에서 위로 블록을 이동시키면 <그림 2>의 상태가 된다.
여기서, 왼쪽으로 블록을 이동시키면 <그림 3>의 상태가 된다.

<그림 4>	<그림 5>	<그림 6>	<그림 7>
<그림 4>의 상태에서 블록을 오른쪽으로 이동시키면 <그림 5>가 되고, 
여기서 다시 위로 블록을 이동시키면 <그림 6>이 된다.
여기서 오른쪽으로 블록을 이동시켜 <그림 7>을 만들 수 있다.

<그림 8>	<그림 9>
<그림 8>의 상태에서 왼쪽으로 블록을 옮기면 어떻게 될까? 2가 충돌하기 때문에,
4로 합쳐지게 되고 <그림 9>의 상태가 된다.
			
<그림 10>	<그림 11>	<그림 12>	<그림 13>
<그림 10>에서 위로 블록을 이동시키면 <그림 11>의 상태가 된다. 

<그림 12>의 경우에 위로 블록을 이동시키면 <그림 13>의 상태가 되는데,
그 이유는 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다.
	
<그림 14>	<그림 15>
마지막으로, 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.
예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다.
<그림 14>의 경우에 위로 이동하면 <그림 15>를 만든다.

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.
보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

예제 입력 1 
3
2 2 2
4 4 4
8 8 8
예제 출력 1 
16
'''

# 그래프가 아닌것같은데?
# 행이랑 열로 나눠서 리스트로 시행마다 저장한 후
# 상하좌우로 쭉 밀었을 때의 값으로 갱신해주는 방식으로 가야할 듯.
'''
N = int(input())

board_2048 = [list(map(int, input().split())) for _ in range(N)]

# 가로세로 변경함수. 대각선으로 뒤집기
def transpose(board):
    transposed = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            transposed[row][col] = board[col][row]
    return transposed

max_num = 0
def play_2048(board, depth):
    global max_num

    if depth == 5:
        return
    
    # prev에 0이 있으면 prev를 num으로 갱신
    # prev와 num이 같으면 2배해서 밀어넣고 prev를 0으로 초기화
    # prev와 num이 다르면 prev를 밀어넣고 prev를 num으로 갱신
    # 마지막에 남은 prev가 0이 아니면 밀어넣기
    # N길이에 맞춰 남은 칸에 0 밀어넣기

    # 왼쪽으로 밀기
    temp_board = []
    for i in range(N):
        temp_row = []
        prev = 0
        for num in board[i]:
            if num != 0:
                if prev == 0:
                    prev = num
                elif prev == num:
                    temp_row.append(num * 2)
                    prev = 0
                else:
                    temp_row.append(prev)
                    prev = num
        if prev != 0:
            temp_row.append(prev)
        temp_row += [0] * (len(board[i]) - len(temp_row))
        temp_board.append(temp_row)
        max_num = max(max_num, max(map(max, temp_board)))
    play_2048(temp_board, depth + 1)

    # 오른쪽으로 밀기
    temp_board = []
    for i in range(N):
        temp_row = []
        prev = 0
        for num in board[i][::-1]:
            if num != 0:
                if prev == 0:
                    prev = num
                elif prev == num:
                    temp_row.append(num * 2)
                    prev = 0
                else:
                    temp_row.append(prev)
                    prev = num
        if prev != 0:
            temp_row.append(prev)
        temp_row = [0] * (len(board[i]) - len(temp_row)) + temp_row
        temp_board.append(temp_row)
        max_num = max(max_num, max(map(max, temp_board)))
    play_2048(temp_board, depth + 1)
    
    transposed = transpose(board)

    # 위로 밀기
    temp_board = []
    for i in range(N):
        temp_row = []
        prev = 0
        for num in transposed[i]:
            if num != 0:
                if prev == 0:
                    prev = num
                elif prev == num:
                    temp_row.append(num * 2)
                    prev = 0
                else:
                    temp_row.append(prev)
                    prev = num
        if prev != 0:
            temp_row.append(prev)
        temp_row += [0] * (len(board[i]) - len(temp_row))
        temp_board.append(temp_row)
        max_num = max(max_num, max(map(max, temp_board)))
    play_2048(transpose(temp_board), depth + 1)

    # 아래로 밀기
    temp_board = []
    for i in range(N):
        temp_row = []
        prev = 0
        for num in transposed[i][::-1]:
            if num != 0:
                if prev == 0:
                    prev = num
                elif prev == num:
                    temp_row.append(num * 2)
                    prev = 0
                else:
                    temp_row.append(prev)
                    prev = num
        if prev != 0:
            temp_row.append(prev)
        temp_row += [0] * (len(board[i]) - len(temp_row))
        temp_board.append(temp_row)
        max_num = max(max_num, max(map(max, temp_board)))
    play_2048(transpose(temp_board), depth + 1)

play_2048(board_2048, 0)
print(max_num)
'''
# 개선할 부분이 많다. 다시 해보자.

import sys
input = sys.stdin.readline

N = int(input())

board_2048 = [list(map(int, input().split())) for _ in range(N)]

# 대각선으로 뒤집기
def transpose(board):
    return [list(row) for row in zip(*board)]

# 좌우로 뒤집기
def reverse_rows(board):
    return [row[::-1] for row in board]

# 왼쪽으로 미는 경우를 정의
def push_left(board):
    # prev에 0이 있으면 prev를 num으로 갱신
    # prev와 num이 같으면 2배해서 밀어넣고 prev를 0으로 초기화
    # prev와 num이 다르면 prev를 밀어넣고 prev를 num으로 갱신
    # 마지막에 남은 prev가 0이 아니면 밀어넣기
    # N길이에 맞춰 남은 칸에 0 밀어넣기
    new_board = []
    for row in board:
        new_row = []
        prev = 0
        for num in row:
            if num != 0:
                if prev == 0:
                    prev = num
                elif prev == num:
                    new_row.append(prev * 2)
                    prev = 0
                else:
                    new_row.append(prev)
                    prev = num
        if prev != 0:
            new_row.append(prev)
        new_row += [0] * (N - len(new_row))
        new_board.append(new_row)
    return new_board

max_num = 0
def play_2048(board, depth):
    global max_num
    # 5번 움직여서 가장 큰 타일을 갱신하고 재귀를 종료한다.
    if depth == 5:
        max_tile = max(map(max, board))
        max_num = max(max_num, max_tile)
        return

    # 왼쪽으로 민 보드로 재귀
    play_2048(push_left(board), depth + 1)

    # 좌우로 뒤집어서 왼쪽으로 밀고 다시 좌우로 뒤집으면 오른쪽으로 민 보드가 된다.
    right_board = push_left(reverse_rows(board))
    play_2048(reverse_rows(right_board), depth + 1)

    # 전치해서 왼쪽으로 밀고 다시 전치하면 위로 민 보드가 된다.
    up_board = transpose(board)
    up_merged = push_left(up_board)
    play_2048(transpose(up_merged), depth + 1)

    # 전치해서 좌우로 뒤집어서 왼쪽으로 밀고 다시 좌우로 뒤집고 전치하면 아래로 민 보드가 된다.
    down_board = reverse_rows(transpose(board))
    down_merged = push_left(down_board)
    play_2048(transpose(reverse_rows(down_merged)), depth + 1)

play_2048(board_2048, 0)
print(max_num)

'''
5
0 0 128 0 8
64 0 0 2 2
2 8 0 0 64
2 32 4 8 8
0 0 0 16 0
'''