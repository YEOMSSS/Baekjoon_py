import sys
input = sys.stdin.readline

N, L = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

result = L

for num in nums:
    if result >= num:
        result += 1
    else:
        break

print(result)