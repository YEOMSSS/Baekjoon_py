'''
문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.

예제 입력 1 
60466175 36
예제 출력 1 
ZZZZZ
'''
'''
# 변환된 B진수의 자릿수 - 1을 찾는 함수
def baser(number, base, i = 0):
    base_multied = base ** i
    if number // base_multied < base:
        return i
    return baser(number, base, i + 1)
    # 이 return이 없으면 None이 반환된다. 앞 호출에서 return이 안 되기 때문.

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, input().split()) # 10진법 N을 B진법 수로 나타내기

for i in range(baser(N, B), 0, -1):
    print(num_list[N // B ** i], end = "")
    N -= (N // B ** i) * B ** i
print(num_list[N])
'''
# 너무 어렵게 풀었는데? 그래도 풀었잖아 한잔해 ☕😎

N, B = map(int, input().split())

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""
while N: # N이 0이 되면 반복문을 종료
    answer += number[N % B] # 가장 낮은 자릿수부터 문자열에 저장됨
    N //= B # N을 B로 한번 나눠줌. B를 i제곱하는것과 동일한 의미

print(answer[::-1]) # 가장 높은 자릿수부터 print 함

# format()도 사용 가능하지만...
# 2, 8, 16진수에서만 가능하다는 제한이 있다.