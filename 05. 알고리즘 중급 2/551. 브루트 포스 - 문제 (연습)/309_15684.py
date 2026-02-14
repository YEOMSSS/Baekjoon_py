# Authored by : marigold2003
# Date : 2026-02-13
# Link : https://www.acmicpc.net/problem/15684


import sys

input = sys.stdin.readline


# [Summary] 사다리 조작

# 사다리타기가 주어진다.
# i번 세로선의 결과가 i번이 나오도록 해야 한다.
# 추가해야 할 가로선의 최소 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 모든 칸에서 만족해야 한다는 게 좀 빡세다.
    # 오, 그래도 3개 이상 그어야 하면 -1출력으로 퉁쳐줬네? 이래서 골3이구나

    # 세로선 10개, 가로선30개까지 가능이라 하면
    # 9*30 = 270. 270 * 269 * 268 = 19464840 단순 브루트포스는 좀 그렇고.

    # 그러면 백트래킹을 써야한다는 것이다. 가지치기를 해야한다.
    # 아 왜이리 감이 안오지? 일단 모든 경우를 확인하긴 해야한다.
    # 근데 사다리 3번 그었다? 종료. i가 i에 도착한다? 종료. 현재 최솟값을 넘어간다? 종료.

    ##########

    # 세로줄개수, 입력될 가로줄개수, 가로줄 칸수
    N, M, H = map(int, input().split())

    ladders = list(list(False for _ in range(N - 1)) for _ in range(H))
    # 사다리가 시작되는 가로위치, 세로위치가 저장됨
    for _ in range(M):
        a, b = map(int, input().split())
        ladders[a - 1][b - 1] = True

    # i번이 i번에 도착하는지 확인하기
    def check() -> bool:
        for c in range(N):
            # 현재 세로줄 위치
            curr = c
            for r in range(H):
                # 좌측 사다리 확인, 있으면 좌로 이동
                if curr > 0 and ladders[r][curr - 1]:
                    curr -= 1
                    # 여기에 continue가 없으면 -=1된 curr가 우측검사에 영향을 받는다.
                    continue
                # 우측 사다리 확인, 있으면 우로 이동
                if curr < N - 1 and ladders[r][curr]:
                    curr += 1
            # i가 i에 도착했다면 다음 세로줄 검사
            if c == curr:
                continue
            return False

        return True

    answer = sys.maxsize

    # 현row, 현col, 사용한 사다리 개수
    def backtrack(prev_r, prev_c, cnt):
        nonlocal answer

        # 현재 최소사용량과 동일하거나 더 많이 사다리를 그었다면 되돌아가기
        # 3개짜리를 성공했다? 그러면 이후부터는 2개짜리만 확인하면 된다.
        if cnt >= answer:
            return

        # 현재 상태 체크, 만족시 되돌아가기
        if check():
            answer = min(answer, cnt)
            return

        # 사다리를 이미 3개 그었으면 되돌아가기
        if cnt == 3:
            return

        # 이전 좌표에서 우로 1열 이동해 사다리 그어보기
        for r in range(prev_r, H):
            # 행 넘어감 처리
            if r == prev_r:
                temp = prev_c
            else:
                temp = 0

            # 열마다 사다리 긋기 시도
            for c in range(temp, N - 1):
                # 좌측이 사다리면 실패
                if c > 0 and ladders[r][c - 1]:
                    continue
                # 현재 칸이 사다리면 실패
                if ladders[r][c]:
                    continue
                # 우측이 사다리면 실패
                if c + 1 < N - 1 and ladders[r][c + 1]:
                    continue

                # 사다리를 그을 수 있다면 긋고, 다음 칸으로 이동한다.
                ladders[r][c] = True
                backtrack(r, c, cnt + 1)
                ladders[r][c] = False

    backtrack(0, 0, 0)
    print(answer if answer != sys.maxsize else -1)

    ##########

    return


# [Review]

# 아 왜이렇게 안풀리지? 이 문제가 내 체감으롤 역대 제일 어려운거같다. 왜일까...
# 그렇게 어려운 문제는 아닌데, 왜 이렇게 어려운 거지??


if __name__ == "__main__":
    main()
