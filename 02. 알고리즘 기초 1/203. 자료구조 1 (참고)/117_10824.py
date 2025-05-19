'''
문제
네 자연수 A, B, C, D가 주어진다. 이때, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.

두 수 A와 B를 합치는 것은 A의 뒤에 B를 붙이는 것을 의미한다. 즉, 20과 30을 붙이면 2030이 된다.

입력
첫째 줄에 네 자연수 A, B, C, D가 주어진다. (1 ≤ A, B, C, D ≤ 1,000,000)

출력
A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.

예제 입력 1 
10 20 30 40
예제 출력 1 
4060
'''
'''
import sys
input = sys.stdin.readline

string = list(input().split())

print(int(string[0] + string[1]) + int(string[2] + string[3]))
'''
# 왜 굳이 리스트를 썼지?

import sys
input = sys.stdin.readline

a, b, c, d = input().split()

# print에서 모든 계산을 하기보다 이렇게 한번 쉬어주는게 좋다.
A = int(a + b)
B = int(c + d) 

print(A + B)