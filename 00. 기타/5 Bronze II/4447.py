
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().rstrip()

    G_cnt = string.upper().count("G")
    B_cnt = string.upper().count("B")

    if G_cnt > B_cnt:
        print(f"{string} is GOOD")
    elif G_cnt < B_cnt:
        print(f"{string} is A BADDY")
    else:
        print(f"{string} is NEUTRAL")