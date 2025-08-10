import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

# (A × B) % M = ((A % M) × (B % M)) % M

result = 1
for num in nums:
    result *= num % M

print(result % M)
