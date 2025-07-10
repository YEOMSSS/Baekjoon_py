import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    if 0 <= X < 24 and 0 <= Y < 60:
        print("Yes", end= " ")
    else:
        print("No", end= " ")

    if 0 < X <= 12:
        if (
            (X in (1, 3, 5, 7, 8, 10, 12) and 0 < Y <= 31) or
            (X in (4, 6, 9, 11) and 0 < Y <= 30) or
            (X == 2 and 0 < Y <= 29)
        ):
            print("Yes")
        else:
            print("No")
    else:
        print("No")