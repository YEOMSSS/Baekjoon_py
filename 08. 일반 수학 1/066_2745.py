'''
문제
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.

예제 입력 1 
ZZZZZ 36
예제 출력 1 
60466175
'''
'''
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 인덱스가 곧 값

# B진법 수 N
N, B = input().split()

answer = 0
for num in N[::-1]: # 한 자리씩 계산해서 answer에 더한다.
    # 치명적 오류: 같은게 여러개 들어오면 N[::-1].index(num)가 고장나!
    answer += num_list.index(num) * (int(B) ** N[::-1].index(num))
    # num_list.index(num)은 N의 일의자리부터 들어온다.
    # B의 N[::-1].index(num) 제곱은 B진법 자릿수 계산법이다.
    # 10진법으로 예시를 들면, 천의자리가 num * 10 ** 3 인 것과 같다.
print(answer)
'''
# 오류를 수정해서 다시 만들어보자.
'''
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split() # B진법 수 N

answer = 0
for i, num in enumerate(N[::-1]):
    answer += num_list.index(num) * int(B) ** i
print(answer)
'''
# 사실 파이썬에서는 훨씬 쉽게 할 수 있다.

N, B = input().split()
print(int(N, int(B)))