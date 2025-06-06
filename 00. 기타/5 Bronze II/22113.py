
import sys

n, m = map(int, input().split())

bus_nums = list(map(int, input().split()))

prices = [list(map(int, val.split())) for val in sys.stdin.read().splitlines()]

ans = 0
for i in range(len(bus_nums) - 1):
    ans += prices[bus_nums[i] - 1][bus_nums[i + 1] - 1]

print(ans)