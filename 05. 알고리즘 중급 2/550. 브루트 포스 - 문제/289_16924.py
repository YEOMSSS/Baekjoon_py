import sys

input = sys.stdin.readline

# 모든 점에 대하여 만들 수 있는 십자가를 찾는다.


def main() -> None:
    N, M = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(N)]

    answer = []

    # 모든 점에 대해 십자가 생성 여부 검사
    for r in range(N):
        for c in range(M):
            if board[r][c] == ".":
                continue

            d = 1
            while True:
                for dr, dc in ((0, -d), (0, d), (-d, 0), (d, 0)):
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        break
                    if board[nr][nc] == ".":
                        break
                # 십자가가 생길 때마다 append
                else:
                    # 중심이 같고 길이가 다른 십자가도 전부 입력됨
                    answer.append((r + 1, c + 1, d))
                    d += 1
                    continue

                break

    result_board = [["." for _ in range(M)] for _ in range(N)]
    for r, c, d in answer:
        r, c = r - 1, c - 1
        result_board[r][c] = "*"
        for dr, dc in ((0, -d), (0, d), (-d, 0), (d, 0)):
            nr, nc = r + dr, c + dc
            result_board[nr][nc] = "*"

    if board == result_board:
        print(len(answer))
        for a in answer:
            print(*a)
    else:
        print(-1)


if __name__ == "__main__":
    main()
