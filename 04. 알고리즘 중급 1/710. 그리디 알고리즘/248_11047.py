
# 그리디 알고리즘의 기초.

import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    result = 0
    for coin in coins[::-1]:
        result += K // coin
        K %= coin

    print(result)

if __name__ == "__main__":
    main()