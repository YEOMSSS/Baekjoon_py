# Authored by : marigold2003
# Date : 2026-03-22
# Link : https://www.acmicpc.net/problem/16932


import sys

input = sys.stdin.readline


# [Summary] 모양 만들기

# N*M(<= 1000) board가 입력된다.
# 각 칸에는 0 or 1이 들어있다.
# 1이 있는 인접한 칸끼리 연결했을 때, 각 요소를 모양이라 한다.

# 배열의 칸 하나에 들어있는 수를 변경해 만들 수 있는
# 모양의 최대 크기를 구하시오.


def main() -> None:

    # [Ideas]

    # 생각나는 게 두가지 있는데, 브루트포스랑 dfs응용.
    # 브루트포스는 주변에 1이 2개 있는 0을 세둬서 그만큼 dfs를 돌려보는거고.
    # 근데 뭔가 느낌이 시간초과다. 삘이 온다. 칸이 1M개인데...

    # dfs응용은, flag를 같이 stack에 넣어서 굴리는거지.
    # 0을 만나면 하나는 사용완료딱지를 붙여 1로 치고서 stack에 넣고
    # 하나는 그냥 0을 무시하고 계속 가던길을 가는 것.
    # 이거 한번 해보자. visited 관리를 어떻게 해야하지?
    # 연장됐을 경우는 넣으면 안될거같은데.

    # 좀 다르게 생각해보자. 통로 후보들을 찾아두는거지.
    # 그게 주변에 1을 2개 이상 가진 0이 될 것이다.
    # 모든 섬에 크기를 일단 구해두고, {그 섬의 어느 칸 : 섬의 크기} 를 저장해두자.
    # 그러면 후보만 봐도 간단한 덧셈으로 찾을 수 있다!
    # 아니면 섬의 번호를 지정해두는것도 괜찮겠지. 이걸로 가보자.

    ##########

    from collections import deque

    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    # 방문시 섬id가 저장된다.
    visited = [[0] * C for _ in range(R)]

    island_size_info = [0]

    def bfs(start, sid):
        island_coords = set()

        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = sid
        island_coords.add(start)

        count = 1

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= R:
                    continue
                if nc < 0 or nc >= C:
                    continue
                if visited[nr][nc]:
                    continue
                if not board[nr][nc]:
                    continue

                queue.append((nr, nc))
                visited[nr][nc] = sid

                count += 1

        island_size_info.append(count)

        return

    sid = 0
    for r in range(R):
        for c in range(C):
            if not board[r][c]:
                continue
            if visited[r][c]:
                continue
            sid += 1
            bfs((r, c), sid)

    answer = 0
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                continue

            tempset = set()

            count = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R:
                    continue
                if nc < 0 or nc >= C:
                    continue
                if not board[nr][nc]:
                    continue
                tempset.add(visited[nr][nc])

            for sid in tempset:
                count += island_size_info[sid]

            answer = max(answer, count)

    print(answer)

    ##########

    return


# [Review]

# 발상이 생각보다 오래 걸렸네?
# 하지만 다음엔 굉장히 쉽게 풀 수 있을 것 같다.


if __name__ == "__main__":
    main()
