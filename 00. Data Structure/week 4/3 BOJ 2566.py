# Authored by : marigold2003
# Date : 2026-03-25
# Link : https://www.acmicpc.net/problem/2566


import sys

input = sys.stdin.readline


# [Summary] 최댓값

# 9*9 board가 주어진다.
# board 내 값의 최댓값을 구하시오.


def main() -> None:

    ##########

    myMap = [list(map(int, input().split())) for _ in range(9)]

    maxval = -1
    whereY, whereX = 0, 0

    # 그냥 9를 쓰는 것과 차이가 없다. 오히려 len비용만 추가됨
    for y in range(len(myMap)):
        for x in range(len(myMap[y])):

            if myMap[y][x] > maxval:
                maxval = myMap[y][x]
                # whereY, whereX = y, x
                whereY = y
                whereX = x

    print(maxval)
    print(whereY + 1, whereX + 1)

    ##########

    return


if __name__ == "__main__":
    main()
