import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())

    result = 0
    for x in range(1, A + 1):
        for y in range(1, B + 1):
            for z in range(1, C + 1):
                if x % y == y % z == z % x:
                    result += 1

    print(result)