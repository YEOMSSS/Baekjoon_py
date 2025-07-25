import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trash_in_row = sum(map(int, input().split()))
trash_in_col = sum(map(int, input().split()))

print(trash_in_row + trash_in_col)