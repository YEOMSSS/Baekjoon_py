import sys

input = sys.stdin.readline


def solve(arr: list) -> list:
    arr.sort(key=lambda x: (x[1], x[0]))
    return arr


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for a in solve(arr):
        print(*a)
