'''
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
620
61
예제 입력 2 
64
65
예제 출력 2 
-1
'''
'''
def prime_judge(val): # 소수 판독기 다시 만들고
    if val == 1:
        return False
    for i in range(2, val):
        if val % i == 0:
            return False
    return True
'''
# 소수 판독기는 제곱근까지만 검사해도 된다고?
# 하긴 약수에서 작은거만 봐도 큰 수가 뭔지 알 수 있으니까.

import math

def prime_judge(val):
    if val < 2:
        return False
    for i in range(2, int(math.sqrt(val)) + 1): # 제곱근에는 내림을 해주자.
        if val % i == 0:
            return False
    return True

M = int(input())
N = int(input())

primes = []
for i in range(M, N + 1):
    if prime_judge(i):
        primes.append(i)
'''
if len(prime_arr) == 0: # 소수 없으면 -1 출력
    print(-1)
else:
    print(sum(prime_arr))
    print(min(prime_arr))   
'''
# 파이썬에서 빈 리스트는 False를 반환한다고?

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))   

# 제곱근까지만 하니 시간초가 훨씬 줄어들었다! 다음엔 에라토스테네스의 체도 써보자.
# prime_list니, prime_arr이니 하지말고 primes가 제일 깔끔한 듯.