import sys

input = sys.stdin.readline

# 같은 행이나 열은 두번 뒤집을 필요가 없다. 원상복구되니까.
# N+N이 뒤집을 수 있는 최대 횟수가 된다.
# 동전을 어떤 순서로 뒤집든 간에 결과는 같다는 게 포인트.

# 000 000 010 010
# 000 111 101 010
# 000 000 010 010
# 2행 2열 2행 순으로 뒤집었을때 처음에서 2열만 뒤집은 결과가 나온다.
# 순서가 바뀌어도 상관 없다.

# 일단 뒤집을 열을 고르는 모든 경우를 브루트포스로 선택한다.
# 그리고 모든 경우에 대해 직접 뒤집어본 후, 뒤집으면 이득인 행만 뒤집는다.


# 오랜만에 빡세게 했다! 역시 알고리즘 문제가 몰입이 잘 된다.
# 다음엔 솔플로 풀 수 있었으면 좋겠네.
def main():
    N = int(input())

    # "THHT" -> int("1001", 2) -> 9. 행을 그대로 압축하여 저장한다.
    rows = [
        int(input().rstrip().replace("H", "0").replace("T", "1"), 2) for _ in range(N)
    ]
    # 11111.... 1이 N개. 토글용.
    full = (1 << N) - 1

    result = N * N

    # 1<<N == 2**N. N개의 비트로 만들 수 있는 모든 경우의 수
    # mask는 comb의 역할을 한다.
    for mask in range(1 << N):
        # 열로 센 뒷면의 개수를 저장
        col_count = [0] * N

        # mask에 담긴 비트 정보에 따라 행을 뒤집는다.
        for i in range(N):
            # i번째 mask가 1이면 i번 row를 토글하여 row에 저장한다.
            # xor 0을 하면 유지, xor full을 하면 전체 토글이 된다.
            row = rows[i] ^ (full if mask & (1 << i) else 0)

            for j in range(N):
                # 처리된 row의 각 비트가 1인지 확인하여 col_count에 누적한다.
                # if row & (1 << j):
                #     col_count[j] += 1

                # row >> j는 j번 rshift하여 j를 lsb가 되게 한다. and 1을 하면 1인지 확인 가능.
                col_count[j] += (row >> j) & 1

        total = 0
        for c in col_count:
            # 뒤집어서 이득일 때만 뒤집는다. c > N//2 일 때 뒤집기와 동일.
            total += min(c, N - c)

        # 최솟값 갱신.
        result = min(result, total)

    print(result)


if __name__ == "__main__":
    main()

# 괜찮긴 한데, 조금만 더 줄여보자.
# 더 직관적으로 비트 저장도 순서가 그대로 눈에 보이게 저장해보자.
"""
def main():
    N = int(input())

    # 비트마스크로 압축한 행을 리스트로 저장한다.
    rows = []
    for _ in range(N):
        s = input().rstrip()
        bits = 0
        for i, c in enumerate(s):
            if c == "T":
                # or 1 로 i번째 비트를 켠다.
                bits |= 1 << i
        rows.append(bits)
    result = N * N

    # 1<<N == 2**N. N개의 비트로 만들 수 있는 모든 경우의 수
    # mask는 comb의 역할을 한다.
    for mask in range(1 << N):
        # 열로 센 뒷면의 개수를 저장
        col_count = [0] * N

        # mask에 담긴 비트 정보에 따라 행을 뒤집는다.
        for i in range(N):
            row = rows[i]
            # mask의 i번째 비트가 1인지 and 1<<i 로 확인한다.
            if mask & (1 << i):
                # i번째 행을 xor 1111...로 토글한다.
                row ^= (1 << N) - 1

            for j in range(N):
                # 처리된 row의 각 비트가 1인지 확인하여 col_count에 누적한다.
                if row & (1 << j):
                    col_count[j] += 1

        total = 0
        for c in col_count:
            # 뒤집어서 이득일 때만 뒤집는다. c > N//2 일 때 뒤집기와 동일.
            total += min(c, N - c)

        # 최솟값 갱신.
        result = min(result, total)

    print(result)


if __name__ == "__main__":
    main()
"""

# 너무 느림. 비트마스크를 사용해야한다.
"""
from itertools import combinations
import copy


def main() -> None:

    # 앞면 0, 뒷면 1로 저장한다.
    N = int(input())
    board = [[1 if c == "T" else 0 for c in input().rstrip()] for _ in range(N)]

    count_T = N * N

    for n in range(N + 1):
        for comb in combinations(range(N), n):
            temp_count = 0
            temp_board = copy.deepcopy(board)

            # 뒤집을 행 토글하기
            for row in comb:
                for col in range(N):
                    temp_board[row][col] ^= 1
            for col_count in map(sum, zip(*temp_board)):
                if col_count > N // 2:
                    temp_count += N - col_count
                else:
                    temp_count += col_count

            count_T = min(count_T, temp_count)

    print(count_T)


if __name__ == "__main__":
    main()
"""
