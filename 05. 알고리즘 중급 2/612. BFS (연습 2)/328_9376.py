# Authored by : marigold2003
# Date : 2026-03-04
# Link : https://www.acmicpc.net/problem/9376


import sys

input = sys.stdin.readline


# [Summary] 탈옥

# 감옥에서 죄수 두 명을 탈출시켜야 한다.
# 벽*, 문#, 빈 공간., 죄수의 위치$가 주어진다.
# board는 h(100)*w(100) 크기이다.
# 두 죄수를 모두 탈옥시키기 위해 필요한 문의 개수의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 둘을 모두 탈출시키는 최솟값이기 때문에, 누구 하나를 우선시할 수 없다.
    # 죄수에서부터 시작하는 건 불가능해 보이고, 탈출가능한 곳에서부터 시작해야한다.
    # 죄수의 위치는 기록만 해 두고, 그냥 빈 공간으로 만들어도 될 듯.

    # 테두리에 있는 문과 빈 공간에서 죄수로 가는 bfs를 짜보자.
    # 음, 약간 생각을 바꿔서, 문을 열면 다음으로 이동 가능한 장소는
    # 이동 가능한 모든 문이 되는거 아닌가? 한칸씩 갈 필요가 없어보이는데?

    # 헷갈린다. 그래도 일단 한칸씩 짜보자. 어차피 테두리는 400칸도 안된다.
    # 아니야, 그러면 안 된다. 이거 최단거리랑 다른문제다.
    # 최단 문이다. 최단 문. 재정의 해야한다. 문에서 문으로 이동해야 한다.
    # 이동할 수 없을 때까지 움직여서 그자리 문을 여는 게 행동 한번이다.
    # padding하고 돌리면 굳이 테두리를 찾을 필요도 없음.

    # 이런걸 편하게 해주는게 01bfs지. 문은 비용1, 빈칸은 비용0. 싼거 우선으로 가자.
    # 빈칸은 appendleft, 문은 append로 처리하자.

    # 출발지를 어떻게 해야할지도 문제다. 밖에서만 시작되는 것도 아닌 것 같다.
    # 밖, 죄수1, 죄수2를 연결하는 점이 있다고 생각해보자.
    # board의 모든 벽과 빈칸에 대해 bfs를 3번씩 돌리면 된다.
    # 그러니까, 밖, 죄수1, 죄수2가 curr빈칸으로 향하는 bfs를 돌리면 되겠지.

    # bfs를 미리 모든 칸에 대해 다 돌려놓는게 좋겠다.
    # 어차피 한칸씩 퍼져나가니까, 미리 모든 칸으로 이동하는 최소비용을 돌려두자.
    # 밖, 죄수1, 죄수2에 대해서 모든 칸으로 이동하는 비용을 구해둔다.

    # 이후 모든 (r, c)에서 밖, 죄수1, 죄수2를 다 더하면 그게 벽뚫최솟값.
    # 벽을 뚫은 최솟값들의 결과들 중에서 최솟값을 찾으면 된다.
    # 아, 벽칸이면 겹친거니까 -2해주는게 포인트.

    ##########

    from collections import deque

    INF = sys.maxsize

    # start에서 각 칸으로 이동하는 최소비용 리스트를 반환
    def bfs(start: tuple[int], board: list[str], R: int, C: int) -> list[int]:
        costs = [[INF] * C for _ in range(R)]
        dq = deque()

        dq.append(start)
        # 자신이 서있는 칸은 당연히 0이다.
        costs[start[0]][start[1]] = 0

        while dq:
            r, c = dq.popleft()

            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nr, nc = r + dr, c + dc

                # 인덱스 초과 시 반환. padding을 했으나 벽으로 한게 아니라 필요한 과정
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                # 벽으로는 이동불가
                if board[nr][nc] == "*":
                    continue

                cost = costs[r][c]
                # 이동할 칸이 문이면 열어야 한다.
                if board[nr][nc] == "#":
                    cost += 1

                # 이동할 칸에 이미 더 싼 비용으로 도착할 수 있으면 이번 경로로 갈 필요가 없다.
                # 더 싼 비용으로 도착한 경우에만 갱신하면 된다. 다익냄새 솔솔
                if costs[nr][nc] > cost:
                    costs[nr][nc] = cost

                    # 벽인 애들은 나중에 처리한다.
                    # 비용이 적은 것부터 우선적으로 처리하는 것이 push횟수를 줄인다.
                    if board[nr][nc] == "#":
                        dq.append((nr, nc))
                    else:
                        dq.appendleft((nr, nc))

        return costs

    T = int(input())

    for _ in range(T):

        R, C = map(int, input().split())
        board_input = [list(input().rstrip()) for _ in range(R)]

        # 일단 padding을 해주자.
        board = [["."] * (C + 2)]
        targets = []

        for r in range(R):
            row = ["."]
            for c in range(C):
                curr = board_input[r][c]

                if curr == "$":
                    # padding이 있으니 +1씩 해준다.
                    targets.append((r + 1, c + 1))
                    row.append(".")
                else:
                    row.append(curr)

            row.append(".")
            board.append(row)

        board.append(["."] * (C + 2))

        R += 2
        C += 2

        # 밖, 죄수1, 죄수2의 cost목록 뽑아오기
        costs_out = bfs((0, 0), board, R, C)
        costs_t1 = bfs(targets[0], board, R, C)
        costs_t2 = bfs(targets[1], board, R, C)

        answer = INF

        # 모든 칸에서 밖, 죄수1, 죄수2로 가는 최소비용을 더한다.
        for r in range(R):
            for c in range(C):

                # 벽에서는 시작할 수 없다.
                if board[r][c] == "*":
                    continue

                total = costs_out[r][c] + costs_t1[r][c] + costs_t2[r][c]

                # curr가 문이면 3개가 겹쳐있으니 2번 빼준다.
                if board[r][c] == "#":
                    total -= 2

                answer = min(answer, total)

        print(answer)

    ##########

    return


# [Review]

# 쉽지만은 않았다.
# 다익냄새 나는 01bfs에, 모든 칸에서 3곳으로 이동하는 건 나름 재밌는 발상이었음.
# padding을 벽이 아닌걸로 해본것도 처음이네.

if __name__ == "__main__":
    main()
