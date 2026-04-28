import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-04-28
# Problem Number : 5108


# [Summary] 5108. [S/W 문제해결 기본] 7일차 - 숫자 추가

# 수열이 주어지고, 수열에 insert할 정보가 주어진다.
# 모든 insert를 완료한 수열에서 원하는 인덱스를 출력하시오.
# 수열 길이는 1K 이하, 추가 횟수는 1K 이하, 원하는 인덱스는 N + M 이하


def main() -> None:

    # [Ideas]

    # 파이썬이니 insert를 그냥 사용하면 된다.
    # 수열의 길이가 작으므로 시간 초과가 나지 않는다.

    ##########

    T = int(input())

    for tc in range(1, T + 1):

        N, M, L = map(int, input().split())
        arr = list(map(int, input().split()))

        for _ in range(M):
            a, b = map(int, input().split())
            arr.insert(a, b)

        print(f"#{tc} {arr[L]}")

    ##########

    return


# [Review]

# insert를 사용하라고 판이 깔려있는 문제.


if __name__ == "__main__":
    main()
