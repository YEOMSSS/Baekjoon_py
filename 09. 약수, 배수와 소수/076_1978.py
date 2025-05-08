'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3
'''

def prime_judge(val):
    if val == 1:
        return False
    for i in range(2, val): # val에 2가 들어오면 작동하지 않는다!
        if val % i == 0:
            return False
    return True

cnt = int(input()) # 의미 없는 한 줄. 그냥 쓰라니까 쓴 거지

prime_list = list(map(int, input().split()))

prime_cnt = 0
for num in prime_list:
    if prime_judge(num):
        prime_cnt += 1

print(prime_cnt)