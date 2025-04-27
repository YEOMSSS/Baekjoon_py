'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1 
1 1
2 3
3 4
9 8
5 2
예제 출력 1 
2
5
7
17
7
'''

# 문제에서 테스트케이스의 수를 정해주지 않았다.
# for문으로 5번 반복해서 예제처럼 뽑으면 오답.
# 때문에 EOF가 들어올 때 종료되도록 설계한다.

# import sys
# input = sys.stdin.readline

# while True:
#     try:
#         x, y = map(int, input().split())
#         print(x + y)
#     except:
#         break

# 이 코드는 사실 좋은 코드는 아니다.
# eof가 들어오면 readline은 빈 문자열을 반환한다.
# 그래서 try에서 EOFError가 아닌 ValueError가 뜬다.
# input(readline)에서 빈 문자열이 반환되고 map에서 오류가 난다.
# 그 후 except로 break되는 코드이다. 되긴 된다는 것.

# 저 코드대로 쓰려면 input을 이용하는 것이 좋다.
# readline은 공백을 반환하지만, input은 바로 EOFError를 띄운다.

# while True:
#     try:
#         x, y = map(int, input().split())
#         print(x + y)
#     except EOFError:
#         break

# 이렇게 하면 EOF를 만나도 종료가 잘 된다는 것.

import sys
input = sys.stdin.readline

while True: # 무한반복 시작
    line = input() # 한 줄 입력받기
    if not line: # line이 빈 문자열이면 종료
        break 
    x, y = map(int, line.split()) # 공백 기준으로 쪼개서 정수변환
    print(x + y)

# 이게 readline을 이용한 괜찮은 코드다.

# --------
# import sys
# input = sys.stdin.readline

# while True:
#     try:
#         x, y = map(int, input().split())
#         print(x + y)
#     except EOFError: 
#         break

# 위 코드는 오류가 터진답니당.
# sys.stdin.readline은 EOFError를 발생시키지 않아요.
# 오직 빈 문자열만 반환한다는거, 기억하세요.