'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
'''
# row까지 신경써야 할까?
# 재귀 한번 돌때마다 줄이 바뀌면 되는거 아닌가?

# 아, 퀸이지! ㅅㅂ대각선이 있구나!!
'''
N = int(input())

# 퀸을 놓을 수 있는 자리를 확인하기 위한 체스판 생성
chess_board = [True] * (N * N)

result = 0

cnt = 0
def N_Queen(row, board):
    global result, cnt
    
    # N번째 행에 퀸을 두는 데 성공하고 재귀가 들어온 경우 누적 (조건만족)
    if row == N:
        result += 1
        return
    
    # start row 에서 가능한 col 한번씩 순회
    for col in range(N):

        if board[row * N + col] == True:
            # 재귀가 시작할 때 수정용 보드 따로 만들기
            temp_board = board[:]

            # col의 8칸 전부 확인 (지나온 row는 신경쓸 필요가 없다.)
            for i in range(row + 1, N):
                temp_board[i * N + col] = False
                cnt+=1

            # 2방향 diag 확인(좌상, 우상은 이미 지나와서 신경쓸 필요가 없다.)
            for i in range(N):
                if row + i < N and col - i >= 0:
                    temp_board[(row + i) * N + col - i] = False
                if row + i < N and col + i < N:
                    temp_board[(row + i) * N + col + i] = False
                cnt+=2

            # 수정된 board로 다음 행 재귀하기
            N_Queen(row + 1, temp_board)

# 0행부터 재귀 시작
N_Queen(0, chess_board)

print(result)
print(cnt)
'''
# 이게 되긴 하는데 너무 오래걸리는 것 같다...
# 1차원으로 수정해야 할 필요성이 느껴진다. 그래도 오래걸리네..
# 쓸데없는 가지를 좀 쳐내야 되는데.
# 답이 없다. 보드를 계속 복사해서는 시간이 너무 오래걸린다.
'''
N = int(input())

# 퀸을 놓을 수 있는 col인지 판단
# 재귀 한번에 체스판을 위에서부터 한 줄씩 볼 것이다.
col_board = [True] * N

# *N이 아니라 *2N을 하는 이유는,
# 차가 음수가 되거나 합이 N을 넘길 수 있기 때문에 넉넉하게 2N으로 만드는 것이다.
left_diag_board = [True] * (2 * N)
right_diag_board = [True] * (2 * N)

result = 0
def N_Queen(row):
    global result
    
    # N-1번째 행에 퀸을 두는 데 성공하고 재귀가 들어온 경우 누적 (조건만족)
    if row == N:
        result += 1
        return
    
    # start row 에서 가능한 col 한번씩 순회
    for col in range(N):
        
        # 놓을 수 있는 col인지 확인한다.
        if (
            col_board[col] == True and
            left_diag_board[row + col] == True and
            right_diag_board[row - col + N] == True
        ):
            # 이번 col에 더이상 놓을 수 없다.
            col_board[col] = False

            # 좌하 대각선 퀸의 x, y값을 서로 더한 값은 전부 같다. 
            left_diag_board[row + col] = False

            # 우하 대각선 퀸의 x, y값을 서로 뺀 값은 전부 같다.
            # row-col이 음수가 될 수 있으니 +N으로 양수로 만들어 사용한다.
            right_diag_board[row - col + N] = False

            N_Queen(row + 1)
        
            col_board[col] = True
            left_diag_board[row + col] = True
            right_diag_board[row - col + N] = True

# 0행부터 재귀 시작
N_Queen(0)

print(result)
'''
# 통과되네.
# 그래도 비트마스킹을 해보자.
'''
# 재귀 최대 15번인데 필요없네.
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())

result = 0
# 전역변수로 비트마스크를 껐다켰다하는건 엄청 비효율적이다. 인자로 넣자.
def N_Queen(row, current, left, right):
    global result 
    
    # N-1번째 행에 퀸을 두는 데 성공하고 재귀가 들어온 경우 누적 (조건만족)
    if row == N:
        result += 1
        return
    
    # start row 에서 가능한 col 한번씩 순회
    for col in range(N):
        
        # col이 켜져 있는 비트인지 좌하, 하, 우하를 확인한다.
        if (
            current & (1 << col) and
            left & (1 << row + col) and
            right & (1 << row - col + N)
        ):
            N_Queen(
                row + 1,
                # 이번 col 비트를 끈다.
                current & ~(1 << col),
                # 좌하 대각선 퀸의 x, y값을 서로 더한 값은 전부 같다.
                left & ~(1 << row + col),
                # 우하 대각선 퀸의 x, y값을 서로 뺀 값은 전부 같다.
                # row-col이 음수가 될 수 있으니 +N으로 양수로 만들어 사용한다.
                right & ~(1 << row - col + N)
            )

# 퀸을 놓을 수 있는 col인지 판단
# 재귀 한번에 체스판을 위에서부터 한 줄씩 볼 것이다.
# 비트마스킹으로 켜져있는 비트 N개를 만든다.
col_board = (1 << N) - 1

# *N이 아니라 *2N을 하는 이유는,
# 차가 음수가 되거나 합이 N을 넘길 수 있기 때문에 넉넉하게 2N으로 만드는 것이다.
diag_board = (1 << 2 * N) - 1
diag_board = (1 << 2 * N) - 1

# 0행부터 재귀 시작
N_Queen(0, col_board, diag_board, diag_board)

print(result)
'''
# 생각해보니 대칭성도 존재한다. N // 2로 시작해서 누적 후 2배하면 된다.
# N이 홀수면 가운데거만 한번 더 해서 더해주고.
# 다 필요없다. 비트마스크 최최종 버전으로 간다.

N = int(input())

result = 0

def N_Queen(row, col_mask, left_diag_mask, right_diag_mask):
    global result

    if row == N:
        result += 1
        return

    # 현재 행에서 가능한 위치 비트 계산 (col, 대각선 충돌 제거)
    # |or연산으로 사용불가인걸 전부 킨 후, ~not연산으로 뒤집어 사용가능한거만 전부 킨다.
    # 이후 &and연산으로 인덱스 초과된 좌하 대각선을 행길이에 맞춰 잘라준다.
    available = ~(col_mask | left_diag_mask | right_diag_mask) & ((1 << N) - 1)

    while available:
        # 가장 오른쪽 1비트만 추출 (가능한 위치 중 하나)
        pos = available & -available
        # 사용한 위치 제거 (available이 전부 꺼질 때까지)
        available -= pos

        N_Queen(
            row + 1,
            col_mask | pos, # pos와의 or연산으로 현재 col비트를 켜서 사용불가하게 한다. (누적됨)
            (left_diag_mask | pos) << 1, # 대각선위치에서 좌측으로 한 칸을 사용불가하게 한다. (누적됨)
            (right_diag_mask | pos) >> 1 # 대각선위치에서 우측으로 한 칸을 사용불가하게 한다. (누적됨)
            # 0b0001 >> 1 을 하면 0b0000이 되어 인덱스 초과 시 자동으로 없어진다.
        )

# 시작 마스크: 아무 자리에도 퀸이 없음
N_Queen(0, 0, 0, 0)

print(result)

'''
print([1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596][int(input())])
'''
