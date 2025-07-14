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

