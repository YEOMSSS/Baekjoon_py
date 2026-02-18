# Authored by : marigold2003
# Date : 2026-02-17
# Link : https://www.acmicpc.net/problem/16985


import sys

input = sys.stdin.readline


# [Summary] Maaaaaaaaaze

# 5*5 board 5개를 쌓아서 3차원 maze를 만들 것이다.
# board는 input으로 주어지며, rotate가 가능하며 대칭은 불가능하다.
# board를 쌓는 순서는 마음대로 할 수 있다.
# 입구와 출구는 서로 가장 멀리 있는 두 좌표이다.

# 가장 적은 이동횟수로 출구에 도달하게끔 maze를 만들었을 때
# 그 이동횟수를 출력하시오.


def main() -> None:

    # [Ideas]

    # 미로의 최단거리는 bfs로 찾을 수 있다. 가지가 좀 여러개긴 할 듯.
    # 하지만 이 부분은 어렵지 않게 해결 가능하다. 5*5*5정도면 뭐.

    # 미로가 생기는 경우의 수를 찾아보자.
    # 한 판당 4종류를 가진다.
    # 순서가 정해져 있다 치면 4*4*4*4*4 = 1024개의 미로.
    # 순서가 정해져 있지 않으니 5*4*3*2*1 * 1024 = 122880

    # bfs 122880회정도는 충분히 할 수 있겠지.
    # 어차피 중간에 막히는 경우도 있을 거고.

    # bruteforce로 된다. 확신한다.

    # TODO
    # 5*5 board의 rotate를 구현

    ##########

    # 5*5 board 5개 저장 [board_type][rotate_type][row][col]
    boards = [[[list(map(int, input().split())) for _ in range(5)]] for _ in range(5)]

    # 주어진 board를 90도 rotate해서 return하는 func
    def rotate90(board):
        new_board = []
        for r in range(5):
            new_board.append(list(board[c][r] for c in range(4, -1, -1)))
        return new_board

    for i in range(5):
        boards[i].append(rotate90(boards[i][0]))
        boards[i].append(rotate90(boards[i][1]))
        boards[i].append(rotate90(boards[i][2]))

    ##########

    from collections import deque
    from itertools import permutations, product

    # 최대 이동 칸수는 5*5*5 = 125칸
    MAX = 126
    # 최소 이동 횟수는 4+4+4 = 12칸
    MIN = 12

    # maze의 길찾기 최단거리를 return하는 func
    def bfs(maze: list) -> int:
        if not maze[0][0][0]:
            return 0
        if not maze[4][4][4]:
            return 0
        queue = deque()
        visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]

        queue.append((0, 0, 0))
        visited[0][0][0] = True

        level = 0
        while queue:
            for _ in range(len(queue)):
                if level >= answer:
                    return 0

                h, r, c = queue.popleft()

                if h == 4 and r == 4 and c == 4:
                    return level

                for dh, dr, dc in (
                    (-1, 0, 0),
                    (1, 0, 0),
                    (0, -1, 0),
                    (0, 1, 0),
                    (0, 0, -1),
                    (0, 0, 1),
                ):
                    nh, nr, nc = h + dh, r + dr, c + dc

                    if nh < 0 or nh >= 5:
                        continue
                    if nr < 0 or nr >= 5:
                        continue
                    if nc < 0 or nc >= 5:
                        continue

                    if visited[nh][nr][nc]:
                        continue
                    if not maze[nh][nr][nc]:
                        continue

                    # print(nh, nr, nc)
                    queue.append((nh, nr, nc))
                    visited[nh][nr][nc] = True

            # 현재 level을 갖는 모든 이동이 끝난 후 다음 이동 시작
            level += 1

        return 0

    answer = MAX
    rotate_type_perm = list(product(range(4), repeat=5))
    # board를 쌓는 순서
    for board_order in permutations(range(5)):
        # 각 board의 rotate type 순서
        for rotate_order in rotate_type_perm:

            # 만들어진 maze [height][row][col]
            maze = [boards[b][r] for b, r in zip(board_order, rotate_order)]
            moves = bfs(maze)
            if not moves:
                continue
            if moves == MIN:
                print(moves)
                return
            # bfs 내부에서 answer 이상인 moves는 backtrack되므로 min을 안써도 된다.
            answer = moves

    print(answer if answer != MAX else -1)

    ##########

    return


# [Review]

# bruteforce와 bfs를 잘 버무린 재밌는 문제


if __name__ == "__main__":
    main()
