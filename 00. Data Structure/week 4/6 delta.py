data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

target = 6

whereY, whereX = 0, 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == target:
            whereY = y
            whereX = x

            # x만 탈출됨. 완전 배열에서 탈출하고 싶다면 flag 필요
            # 그냥 함수로 만들어서 return이 쓰고싶긴 하다.
            break

# 상하좌우를 뱉는다.
for dir in range(4):
    newY = whereY + dy[dir]
    newX = whereX + dx[dir]
    # 인덱스에러 처리
    if 0 <= newY < 5 and 0 <= newX < 5:
        print(data[newY][newX])

print(whereY, whereX)
