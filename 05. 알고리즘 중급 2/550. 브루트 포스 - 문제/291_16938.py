import sys

input = sys.stdin.readline

# 15개 중 2~15개를 뽑는 경우의 수
# 2**15 - 1 - 15개. 대충 32K개쯤. 브루트포스 가능

from itertools import combinations


def main() -> None:
    N, L, R, X = map(int, input().split())
    levels = list(map(int, input().split()))

    # 정렬해두면 모든 조합에서 [0]이 최솟값, [-1]이 최댓값이 된다.
    levels.sort()

    if N <= 1:
        print(0)
        return

    count = 0
    for n in range(2, N + 1):
        for comb in combinations(levels, n):
            # 조건 확인. LR사이에 총합, 최대최소차이 X보다큼
            total = sum(comb)
            if L <= total <= R and comb[-1] - comb[0] >= X:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
