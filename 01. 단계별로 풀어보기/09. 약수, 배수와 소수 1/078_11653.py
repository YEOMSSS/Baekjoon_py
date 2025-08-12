'''
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

예제 입력 1 
72
예제 출력 1 
2
2
2
3
3
예제 입력 2 
3
예제 출력 2 
3
예제 입력 3 
6
예제 출력 3 
2
3
예제 입력 4 
2
예제 출력 4 
2
예제 입력 5 
9991
예제 출력 5 
97
103
'''
'''
def prime_judge(val):
    if val < 2:
        return False
    for i in range(2, (val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

num = int(input())

for i in range(2, (num ** 0.5) + 1):
    if prime_judge(i):
        while num % i == 0:
            print(i)
            num //= i

if num != 1:
    print(num)
'''
# 소인수분해 역시, 소수와 같은 개념으로 num ** 0.5를 사용한다. sqrt.math(num)
# 만약 제곱근까지의 소수들로 더 이상 나눠지지 않는데 남은 수가 제곱근보다 크다면?
# 남은 수가 소수라는 뜻이다. 111은 3 * 37 이거든. 

num = int(input())
while True:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(i)
            num //= i
            break # 이 break는 for문을 탈출한다. 그리고 다시 while이 돌아간다.
    else:
        break # 이 break는 while을 탈출한다.
if num != 1:
    print(num)

# 존나 깔끔한 코드다. 두고두고 기억하자.