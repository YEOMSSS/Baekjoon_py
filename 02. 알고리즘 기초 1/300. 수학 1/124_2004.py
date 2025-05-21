'''
문제
 $n \choose m$의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 $n$, $m$ ($0 \le m \le n \le 2,000,000,000$, $n \ne 0$)이 들어온다.

출력
첫째 줄에 $n \choose m$의 끝자리 $0$의 개수를 출력한다.

예제 입력 1 
25 12
예제 출력 1 
2
'''
# nCm 을 구하는 것이다.
# nCm = nPm / m! = n! / ((n - m)! * m!)
'''
import math

n, m = map(int, input().split())

nCm = math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

answer = 0
for char in str(nCm)[::-1]:
    if char != "0":
        break
    else:
        answer += 1

print(answer)
'''
# 그냥 조건이 작다 치고 만든 코드일 뿐.
# 십억이 넘어가는데 전체를 다 계산하는 건 너무 숫자가 커.
# 뒤에 있는 0이잖아? 이건 2*5가 되면서 생기는 거지..
# 수식에서 2와 5만 뽑아서 따로 계산해 내는 거다.
# 2가 곱해진 횟수와 5가 곱해진 횟수 중 작은 쪽이 0이 뒤에 나온 횟수다.

# 10! 에 2가 몇번 곱해졌는지를 어떻게 알지?
# 1*2*3*4*5*6*7*8*9*10 이니까. 2의배수로 5개, 4의배수로 2개, 8의배수로 1개.
# 이런 패턴이 있구만?
'''
def fact_counter(num, target):
    count = 0
    i = 1
    while num >= (target ** i):
        count += num // (target ** i)
        i += 1
    return count


n, m = map(int, input().split())

two_count = fact_counter(n, 2) - fact_counter((n - m), 2) - fact_counter(m, 2)
five_count = fact_counter(n, 5) - fact_counter((n - m), 5) - fact_counter(m, 5)
# n! / ((n - m)! * m!) 제곱끼리는 뺄셈이 되니까.

print(min(two_count, five_count))
'''
# def 부분이 조금 더 최적화가 가능하다고...?

# def fact_counter(num, target):
#     count = 0
#     i = 1
#     while num >= (target ** i):
#         count += num // (target ** i)
#         i += 1
#     return count
# # 10//2 10//4 10//8 | 5, 2, 1

import sys
input = sys.stdin.readline

# Legendre's Formula
def fact_counter(num, target):
    count = 0
    while num:
        num //= target
        count += num
    return count
# 10//2 5//2 2//2 1//2 | 5, 2, 1, 0

n, m = map(int, input().split())

two_count = fact_counter(n, 2) - fact_counter((n - m), 2) - fact_counter(m, 2)
five_count = fact_counter(n, 5) - fact_counter((n - m), 5) - fact_counter(m, 5)
# n! / ((n - m)! * m!) 제곱끼리는 뺄셈이 되니까.

print(min(two_count, five_count))
