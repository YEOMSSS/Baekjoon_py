import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-03-15
# Problem Number : 4831


# [Summary] 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

# 전기버스가 충전 상태로 0에서 출발한다.
# M개의 정류장에 충전기가 설치되어 있다.
# 1회 충전으로 K개의 정류장을 이동할 수 있다.
# N(<= 100)번 정류장까지 가는 최소 충전 횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션이다.
    # 이동가능한 칸에 충전기가 있는지 확인해야 한다.
    # 가장 끝에 있는 충전기를 선택해야 가장 멀리 갈 수 있다. 그리디 냄새가 난다.

    ##########

    T = int(input())

    for tc in range(1, T + 1):
        K, N, M = map(int, input().split())

        route = [False] * (N + 1)
        route[0] = True
        charger = list(map(int, input().split()))
        for c in charger:
            route[c] = True

        count = 0
        # 현재 이동가능한 최대거리
        curr = K

        # 최대거리에 N이 포함될 때까지 검사
        while curr < N:
            for i in range(curr, curr - K, -1):
                # 충전기가 있으면 break
                if route[i]:
                    count += 1
                    curr = i + K
                    break

            # 목적지에 도달하지 못했으나 충전기가 없으면 실패
            else:
                print(f"#{tc} {0}")
                break

        # break 없이 curr가 N을 넘어가서 종료되면 성공
        else:
            print(f"#{tc} {count}")

    ##########

    return


# [Review]

# 풀이가 다양할 것 같다.


if __name__ == "__main__":
    main()
