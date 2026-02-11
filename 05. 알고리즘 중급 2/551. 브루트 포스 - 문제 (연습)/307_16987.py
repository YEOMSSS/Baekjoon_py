# Authored by : marigold2003
# Date : 2026-02-11
# Link : https://www.acmicpc.net/problem/16987


import sys

input = sys.stdin.readline


# [Summary] 계란으로 계란치기

# 왼쪽 계란부터 순서대로 집어 남은 계란 중 하나를 친다.
# 깰 수 있는 계란의 최대 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 그리디처럼 보이지만, 이건 브루트포스다.
    # 무조건 작은 계란을 깬다고 다 좋은것도 아니고, 공격력이 낮은 계란을 깬다고 좋은것도 아니다.

    # 계란이 최대 8개니까, 7*7*7*7*7*7*7*7을 하면 된다. 5764801회다. 백트래킹은 필요해보임.

    # 든 계란이 깨진 경우는 그냥 다음 계란으로 넘어가면 되고
    # 칠 계란이 깨진 경우 이후는 확인할 필요가 없다. 재귀돌려야겠다
    # 구현만 잘하면 될 듯.

    ##########

    N = int(input())
    # 내구력, 공격력 순
    egg_informations = list(list(map(int, input().split())) for _ in range(N))

    answer = 0

    def backtrack(curr):
        nonlocal answer

        # 마지막 계란까지 처리한 후 answer 갱신
        if curr == N:
            count = 0
            for hp in [egg[0] for egg in egg_informations]:
                if hp <= 0:
                    count += 1
            answer = max(answer, count)
            return

        # 현재 차례의 계란이 깨져있는 경우 다음 계란으로 이동
        if egg_informations[curr][0] <= 0:
            backtrack(curr + 1)
            return

        # 현재 차례의 계란만 남아있는 경우 바로 판정으로 이동
        count = 0
        for hp in [egg[0] for egg in egg_informations]:
            if hp <= 0:
                count += 1
        # 현재 차례의 계란은 깨지지 않았기 때문에, 깨진 계란이 N-1개인지 확인하면 된다.
        if count == N - 1:
            backtrack(N)
            return

        # 남아있는 모든 계란에 부딪혀보기
        for i in range(N):
            # 자신과 부딪힐 수 없다.
            if i == curr:
                continue
            # 깨진 계란에 부딪힐 수 없다.
            if egg_informations[i][0] <= 0:
                continue

            # 체력을 서로의 공격력만큼 까고, 백트래킹 후 다시 채워 원상복귀 시켜준다.
            egg_informations[curr][0] -= egg_informations[i][1]
            egg_informations[i][0] -= egg_informations[curr][1]
            backtrack(curr + 1)
            egg_informations[curr][0] += egg_informations[i][1]
            egg_informations[i][0] += egg_informations[curr][1]

    backtrack(0)
    print(answer)

    ##########

    return


# [Review]

# 재귀 백트래킹 연습용 문제. dfsR 백트래킹
# 재밌게 구현했다.


if __name__ == "__main__":
    main()
