#250517
'''
cnt = int(input())

for i in range(cnt):
    print(i + 1)
'''
# 더 빠르게
import sys
input = sys.stdin.readline

answers = list(range(1, int(input()) + 1))
print("\n".join(map(str, answers)))