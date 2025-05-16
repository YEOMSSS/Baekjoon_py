# ( 1 ) 0회
# ( ) 1 1회
# 1 ( ) 1회
# 1 ) ( 1회
# ) ( 1 1회
# ) 1 ( 2회
# 이렇게 6개 경우다.

import sys
input = sys.stdin.readline

match input().strip():
    case "(1)":
        print(0)
    case ")1(":
        print(2)
    case _:
        print(1)