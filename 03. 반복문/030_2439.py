'''
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

예제 입력 1 
5
예제 출력 1 
    *
   **
  ***
 ****
*****
'''

import sys
input = sys.stdin.readline

count = int(input())

for i in range(count):
    # print(" " * (count - (i + 1)), end = "")
    # print("*" * (i + 1))
    print(" " * (count - (i + 1)) + "*" * (i + 1))
    # 위의 둘을 이렇게 합칠 수 있다.

# a = i = int(input())
# while i: # i가 0이 되기 전까지 반복
#     i -= 1
#     print(' ' * i + '*' * (a - i))
# while사용시의 코드.