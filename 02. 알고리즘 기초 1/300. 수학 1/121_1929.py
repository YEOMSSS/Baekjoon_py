'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1 
3 16
예제 출력 1 
3
5
7
11
13
'''
'''
import sys
input = sys.stdin.readline

def prime_judge(val):
    if val == 1:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N + 1):
    if prime_judge(i):
        print(i)
'''
# 체를 써야겠다.

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

sieve = [True] * (N + 1) # 판정할 수까지 일단 체를 만들어. 0포함이니까 +1
sieve[0] = sieve[1] = False # 0, 1은 소수가 아니니까

for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, N + 1, i): # i만큼 건너뛰며 없애면 i의 배수가 사라진다.
            sieve[j] = False

for i in range(M, N + 1):
    if sieve[i]:
        print(i)