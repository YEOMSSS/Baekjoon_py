import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())

string = input().rstrip()

string_count = Counter(string)
string_count_C = string_count["C"]

# 올림 나눗셈: (x + y - 1) // y
print((string_count_C + (N - string_count_C + 1) - 1) // (N - string_count_C + 1))