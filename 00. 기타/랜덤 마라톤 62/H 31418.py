import sys
input = sys.stdin.readline

W, H, K, T = map(int, input().split())

# 어차피 바이러스가 생긴게 다 다르다.
# 1초가 지날 때마다 어디로 이동할 수 있는 칸이 몇개인지 각각 세서 다 곱해주자.
# 1초가 지나면 9칸이 있다. 인덱스 초과하면 그만큼 빠진다.
# 2초가 지나면 25칸, 인덱스 신경쓰기.

MOD = 998_244_353

result = 1
for _ in range(K):
    x, y = map(int, input().split())

    left  = min(T, x - 1)
    right = min(T, W - x)
    up    = min(T, y - 1)
    down  = min(T, H - y)

    ways = (left + right + 1) * (up + down + 1) % MOD
    result = (result * ways) % MOD

print(result)