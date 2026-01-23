import sys

input = sys.stdin.readline


# 파이썬은 정렬이 정말 쉬운 언어구나.


def solve(arr: list) -> list:
    arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    return arr


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(input().split())
        arr.append([temp[0]] + list(map(int, temp[1:])))

    print("\n".join(a[0] for a in solve(arr)))
