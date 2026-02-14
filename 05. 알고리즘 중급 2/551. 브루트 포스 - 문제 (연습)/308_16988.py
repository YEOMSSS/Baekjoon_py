# Authored by : marigold2003
# Date : 2026-02-12
# Link : https://www.acmicpc.net/problem/16988


import sys

input = sys.stdin.readline


# [Summary] Baaaaaaaaaduk2 (Easy)

# 바둑판에 내돌1과 상대돌2가 놓여져 있다.
# 상대돌2를 내돌1을 2개 더 두어 따먹을 수 있는 최대 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 보드를 전부 1로 감싸서 padding을 해놓고 풀자.

    # 2에서 2를 따라가며 보드를 확인해서, 1로 둘러싸여있는지 확인하자.
    # 0으로 도달할 수 있는 경우 종료하면 될 듯.
    # visited배열은 공유하자. 2인 경우만 이동할 것.
    # 그렇게 해서 visited가 아닌 모든 2에서 시작하자.

    # 1로 둘러싸인 2를 찾으면 되는 문제로 정리 가능.

    ##########

    N, M = map(int, input().split())
    # padding
    board = (
        [[1] * (M + 2)]
        + list([1] + list(map(int, input().split())) + [1] for _ in range(N))
        + [[1] * (M + 2)]
    )

    # 0 좌표찾기 (돌을 둘 수 있는 공간)
    coord_zero = []
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if board[r][c] == 0:
                coord_zero.append((r, c))

    from collections import deque

    # 아 씨, 섬찾기는 dfs가 더 편한데. 몰라~ 똑같지 뭐.
    # 아, 1로 둘러싸여졌는지 확인하려면 bfs 써야하네? 뭐야 잘했네
    def solve():
        # queue도 재활용하자.
        queue = deque()
        visited = set()

        result = 0

        for r in range(1, N + 1):
            for c in range(1, M + 1):

                # 방문한 섬의 좌표면 continue
                if (r, c) in visited:
                    continue
                # 값이 2일때만 탐색가능
                if board[r][c] == 1:
                    continue
                if board[r][c] == 0:
                    continue

                # 현재 값이 2이므로 섬의 넓이는 1에서 시작
                count = 1
                visited.add((r, c))
                queue.append((r, c))

                meet_zero = False
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = curr_r + dr, curr_c + dc

                        if (nr, nc) in visited:
                            continue
                        # 1은 벽이다. 벽으로 둘러싸인 섬을 찾는다.
                        if board[nr][nc] == 1:
                            continue
                        # 0을 만났다고 바로 break하지 말고, 일단 flag만 켜두고 섬찾기는 완료하자.
                        if board[nr][nc] == 0:
                            meet_zero = True
                            continue

                        count += 1
                        visited.add((nr, nc))
                        queue.append((nr, nc))

                # 벽으로 감싸져있지 않고 뚫려 0을 만났다면 세지 않는다.
                if not meet_zero:
                    result += count

        return result

    answer = 0
    # 둘 돌 2개 고르기
    cnt_zero = len(coord_zero)
    for i in range(cnt_zero):
        for j in range(i + 1, cnt_zero):
            board[coord_zero[i][0]][coord_zero[i][1]] = 1
            board[coord_zero[j][0]][coord_zero[j][1]] = 1

            answer = max(answer, solve())

            board[coord_zero[i][0]][coord_zero[i][1]] = 0
            board[coord_zero[j][0]][coord_zero[j][1]] = 0

    print(answer)

    ##########

    return


# [Review]

# bfs를 이용해 1로 둘러싸인 섬 찾기
# 백트래킹으로 그래프 순회하기


if __name__ == "__main__":
    main()
