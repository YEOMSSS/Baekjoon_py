import sys
input = sys.stdin.readline

N, L = map(int, input().split())

zebra_list = []
for _ in range(N):
    zebra = input().rstrip()
    lines = zebra.count("10")
    if zebra[-1] == "1":
        lines+= 1
    zebra_list.append(lines)

max_line = max(zebra_list)
print(max_line, zebra_list.count(max_line))