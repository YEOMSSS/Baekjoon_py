# 쓰레기 문제.

import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

# 0 위치 찾기
zr = zc = -1
for r in range(N):
    for c in range(N):
        if board[r][c] == 0:
            zr, zc = r, c
            break
    if zr != -1:
        break

# 목표 합: 0이 없는 아무 행의 합(문제 조건상 0은 정확히 1개라고 가정)
target_row = None
for r in range(N):
    if 0 not in board[r]:
        target_row = r
        break

# 만약 모든 행에 0이 있다면(이론상 불가에 가깝지만) 다른 기준으로 보완
if target_row is None:
    # 0이 없는 열을 찾아서 그 합을 목표 합으로 사용
    target_col = None
    for c in range(N):
        col_vals = [board[r][c] for r in range(N)]
        if 0 not in col_vals:
            target_col = c
            break
    if target_col is None:
        print(-1)
        sys.exit(0)
    target_sum = sum(board[r][target_col] for r in range(N))
else:
    target_sum = sum(board[target_row])

# 0이 있는 행/열의 현재 합
row_sum_with_zero = sum(board[zr])
col_sum_with_zero = sum(board[r][zc] for r in range(N))

# 채워야 할 값
missing = target_sum - row_sum_with_zero

# 자연수(또는 양수) 제약이 있는 문제들이 많음 → 1 이상 체크
if missing <= 0:
    print(-1)
    sys.exit(0)

# 실제로 채워서 검증
board[zr][zc] = missing

# 모든 행/열 검사
for r in range(N):
    if sum(board[r]) != target_sum:
        print(-1)
        sys.exit(0)

for c in range(N):
    if sum(board[r][c] for r in range(N)) != target_sum:
        print(-1)
        sys.exit(0)

# 대각선 검사
diag1 = sum(board[i][i] for i in range(N))
diag2 = sum(board[i][N-1-i] for i in range(N))
if not (diag1 == target_sum and diag2 == target_sum):
    print(-1)
    sys.exit(0)

print(missing)

# 되는지만 보자.

# 안 풀어, 쓰레기 같은 문제. 똑바로 문제를 내야지.
# 0이 당연히 한칸일 거라고 생각되잖아. 시간 낭비했다.