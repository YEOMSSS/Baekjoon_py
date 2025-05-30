# 이항 계수
'''
문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

출력
 \(\binom{N}{K}\)를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
'''
# nCk 구하라는거다. 조합문제임.
# n! / (n-k)! * k!
'''
n, k = map(int, input().split())

def fact(num):
    ans = 1
    for i in range(2, num + 1):
        ans *= i
    return ans

answer = fact(n) // (fact(n - k) * fact(k))
print(answer)
'''
# 그냥 조합의 원리로도 구할 수 있지 않을까?
# 5C2 = 5 * 4 // 2 * 1 니까.

n, k = map(int, input().split())

if k > n - k:
    k = n - k

numer = 1
for i in range(n, n - k, -1): # n ~ n-k+1
    numer *= i
denom = 1
for i in range(k, 0, -1): # k ~ 1
    denom *= i

print(numer // denom)