'''
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

예제 입력 1 
1 2 3 4 5 6 7 8
예제 출력 1 
ascending
예제 입력 2 
8 7 6 5 4 3 2 1
예제 출력 2 
descending
예제 입력 3 
8 1 7 2 6 3 5 4
예제 출력 3 
mixed
'''
# 250517
# 너무쉬운데 이거 이렇게푸는게 맞나

import sys
input0 = sys.stdin.readline

string = input()

match string:
    case "1 2 3 4 5 6 7 8":
        print("ascending")
    case "8 7 6 5 4 3 2 1":
        print("descending")
    case _:
        print("mixed")