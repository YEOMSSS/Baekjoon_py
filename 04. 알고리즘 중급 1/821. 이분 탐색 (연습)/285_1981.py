import sys

input = sys.stdin.readline


# mid로 이 그래프를 통과 가능한지 판정하면 된다. bfs로 해볼까

# 문제가 생겼다. 틀린 경로로 지나간 점이 visited 판정되어서 옳은 경로에서 지나갈 수 없게 된다.
# mid만큼의 차이로 존을 펼쳐 그 안에 들어 있어야만 이동할 수 있도록 해보자.
# 최솟값 ~ 최솟값+mid 부터 해서 최댓값-mid ~ 최댓값까지 전부 돌려본다.


from collections import deque

# 상하좌우
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


# low ~ high 범위 내에 있는 칸만 밟고 도달 가능한지 bfs로 판정한다.
def bfs(board: list, low, high, N) -> bool:

    if not low <= board[0][0] <= high:
        return False

    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    visited[0][0] = True
    queue.append((0, 0))

    while queue:
        r, c = queue.popleft()

        if r == N - 1 and c == N - 1:
            return True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc]:
                continue

            # low ~ high 사이에 있으면 이동 가능
            if low <= board[nr][nc] <= high:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return False


# 판정용 함수
def check(board: list, board_max, board_min, mid, N) -> bool:

    start = board[0][0]
    end = board[-1][-1]

    # low ~ high가 될 수 있는 모든 범위를 mid로 만든다.
    # bmin ~ bmin + mid 부터 bmax - mid ~ bmax 까지 전부 bfs를 돌려 확인한다.
    for low in range(board_min, board_max - mid + 1):
        high = low + mid

        # 시작점, 끝점 포함 여부 확인
        if start < low or end > high:
            continue

        if bfs(board, low, high, N):
            return True

    return False


# mid로 이동가능한 경로가 존재하는지 판정하는 이분탐색
def b_search(board: list, N) -> int:

    # 보드 내에서의 최댓값과 최솟값을 구해둔다.
    board_max = max(map(max, board))
    board_min = min(map(min, board))

    left = 0
    right = board_max - board_min

    result = right

    while left <= right:
        mid = (left + right) // 2

        # mid 이하의 차이로 그래프를
        # 통과가 가능하면 줄여본다.
        if check(board, board_max, board_min, mid, N):
            right = mid - 1
            result = mid
        # 통과가 불가능하면 늘려야만 한다.
        else:
            left = mid + 1

    return result


def solve() -> None:
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(b_search(board, N))


if __name__ == "__main__":
    solve()
