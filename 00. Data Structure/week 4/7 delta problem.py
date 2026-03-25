from random import randint


# 절댓값 func
def myAbs(a):
    return a if a > 0 else -a


# 인덱스 검사 func
def isSafe(y, x) -> bool:
    return 0 <= y < 5 and 0 <= x < 5


data = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

total = 0  # sum은 좀 거부감이
for y in range(5):
    for x in range(5):

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if isSafe(ny, nx):
                total += myAbs(data[y][x] - data[ny][nx])
print(total)
