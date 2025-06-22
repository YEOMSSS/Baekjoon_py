import sys
input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    operation = input().split()
    match operation[0]:
        case "add":
            S.add(operation[1])
        case "remove":
            S.discard(operation[1])
        case "check":
            if operation[1] in S:
                print(1)
            else:
                print(0)
        case "toggle":
            if operation[1] in S:
                S.discard(operation[1])
            else:
                S.add(operation[1])
        case "all":
            S = set(map(str, range(1, 21)))
        case "empty":
            S = set()