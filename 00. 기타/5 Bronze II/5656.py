import sys
input= sys.stdin.readline

i = 0

while True:
    X, symb, Y = input().split()
    if symb == "E":
        break
    i += 1

    X = int(X)
    Y = int(Y)
    result = False
    match symb:
        case ">":
            if X > Y:
                result = True
        case ">=":
            if X >= Y:
                result = True
        case "<":
            if X < Y:
                result = True
        case "<=":
            if X <= Y:
                result = True
        case "==":
            if X == Y:
                result = True
        case "!=":
            if X != Y:
                result = True

    if result:
        print(f"Case {i}: true")
    else:
        print(f"Case {i}: false")

    