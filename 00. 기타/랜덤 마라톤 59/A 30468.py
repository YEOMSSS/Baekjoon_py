STR, DEX, INT, LUX, N = map(int, input().split())

total = STR + DEX + INT + LUX
target = N * 4

if target > total:
    print(target - total)
else:
    print(0)