import sys
input = sys.stdin.readline

answer = 0
total = 0
for _ in range(10):
    a, b = map(int, input().split())
    total += - a + b
    answer = max(answer, total)

print(answer)