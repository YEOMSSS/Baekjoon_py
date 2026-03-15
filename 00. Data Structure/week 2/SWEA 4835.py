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
# Problem Number : 4835


# [Summary] 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

# N(<= 100)개의 정수가 들어있는 배열에서
# 이웃한 M개의 합의 최댓값과 최솟값의 차를 출력하시오.


def main() -> None:

    # [Ideas]

    # 슬라이딩 윈도우로 누적하면서 수를 구해주자.

    ##########

    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))

        left = 0
        right = M

        curr = sum(arr[:right])

        # 최댓값과 최솟값 전부 초기상태
        max_sum = curr
        min_sum = curr

        # 더 늘릴 수 없을 때까지 right 늘리기
        while right < N:

            # 좌측 한칸 줄이기
            curr -= arr[left]
            left += 1

            # 우측 한칸 늘리기
            curr += arr[right]
            right += 1

            # 최댓값 최솟값 갱신
            max_sum = max(max_sum, curr)
            min_sum = min(min_sum, curr)

        print(f"#{tc} {max_sum - min_sum}")

    ##########

    return


# [Review]

# 투포인터의 인덱스 실수를 조심하자.


if __name__ == "__main__":
    main()
