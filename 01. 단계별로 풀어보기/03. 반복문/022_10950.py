'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1 
5
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

count = int(input())

for i in range(count):
    x, y = map(int, input().split())
    print(x + y)

# import sys
# n = int(input())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# sys.stdin.readline을 사용하면 더 빠르다.
# 나중에 시간초과가 나지 않게 해줌.
# 짧은 코드에서는 그냥 input을 사용해도 좋아용.