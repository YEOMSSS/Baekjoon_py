import sys
input = sys.stdin.readline

N = int(input())

integers = map(int, input().split())

answer = 0
for num in integers:
    answer += num if N > num else N

print(answer)