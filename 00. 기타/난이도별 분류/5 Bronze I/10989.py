'''
import sys
input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

nums.sort()

print("\n".join(map(str, nums)))
'''

# 메모리 제한에 걸리네??
# 횟수를 저장해볼까?

import sys
input = sys.stdin.readline

num_counter = [0] * 10001

N = int(input())

for _ in range(N):
    num = int(input())
    num_counter[num] += 1

for i, num_count in enumerate(num_counter):
    if num_count != 0:
        for _ in range(num_count):
            print(i)