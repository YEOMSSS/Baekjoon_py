import sys
input = sys.stdin.readline

N, M = map(int, input().split())

picture = [list(input().rstrip()) for _ in range(N)]
new_picture = [[] for _ in range(M)]

for row in range(N):
    for col in range(M):
        match picture[row][col]:
            case ".":
                new_picture[col].append(".")
            case "O":
                new_picture[col].append("O")
            case "-":
                new_picture[col].append("|")
            case "|":
                new_picture[col].append("-")
            case "/":
                new_picture[col].append("\\")
            case "\\":
                new_picture[col].append("/")
            case "^":
                new_picture[col].append("<")
            case "<":
                new_picture[col].append("v")
            case "v":
                new_picture[col].append(">")
            case ">":
                new_picture[col].append("^")

for line in new_picture[::-1]:
    print("".join(line))