from collections import Counter
import sys
input = sys.stdin.readline

wrong_list = []
result = [0, 0]
while True:
    temp = input().split()
    if temp == ["-1"]:
        break

    M, P, R = temp

    if R == "wrong":
        wrong_list.append(P)
    elif R == "right":
        result[0] += 1
        result[1] += int(M) + (wrong_list.count(P) * 20)

print(*result)