import sys

MOD = 998_244_353
data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
W = next(it); H = next(it); K = next(it); T = next(it)

result = 1
for _ in range(K):
    X = next(it); Y = next(it)

    left = X - 1
    if left > T: left = T
    right = W - X
    if right > T: right = T
    up = Y - 1
    if up > T: up = T
    down = H - Y
    if down > T: down = T

    ways_x = (left + right + 1) % MOD
    ways_y = (up + down + 1) % MOD

    result = (result * (ways_x * ways_y % MOD)) % MOD

print(result)