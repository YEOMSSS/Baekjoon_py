'''
import sys
input = sys.stdin.readline

cycle_dict = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    last_digit = A % 10
    cycle = cycle_dict[last_digit]
    index = (B - 1) % len(cycle)
    print(cycle[index])
'''

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    result = pow(A, B, 10)
    print(10 if result == 0 else result)