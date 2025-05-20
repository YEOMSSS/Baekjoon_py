'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72
'''
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

for i in range(int(min(a, b)) + 1, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        print(int(a * b / i))
        break
'''
# gcd(a, b) * lcm(a, b) = a * b 이다.
# math.gcd(a, b) 는 최대공약수를 찾는다.
# math.lcm(a, b) 는 최소공배수를 찾는다.
'''
import sys
input = sys.stdin.readline

import math

a, b = map(int, input().split())

gcd = math.gcd(a, b)
lcm = math.lcm(a, b)

print(gcd)
print(lcm)
'''
# 유클리드 호제법을 연습해보자.
# a가 b보다 클 때 gcd(a,b)=gcd(b,a%b) 를 반복해서 b가 0일 때 a가 최대공약수이다.

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

a, b = max(A, B), min(A, B)

while b != 0:
    a, b = b, a % b

print(a)
print(A * B // a) # 정수 나눗셈은 int()를 씌우기보다는 //로 나눠주자.

