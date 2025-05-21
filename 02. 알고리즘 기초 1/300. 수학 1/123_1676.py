'''
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1 
10
예제 출력 1 
2
예제 입력 2 
3
예제 출력 2 
0
'''
'''
num = int(input())

answer = 1
for i in range(1, num + 1):
    answer *= i

print(str(answer).count("0"))
'''
# 뒤에서부터 처음 0이 아닌 수가 나올 때까지 0의 개수를 구하라는 건
# 끝에 붙어있는 0의 개수만 세라는 것이었던 거냐.

num = int(input())

fact = 1
for i in range(1, num + 1):
    fact *= i

answer = 0
for char in str(fact)[::-1]:
    if char != "0":
        break
    else:
        answer += 1

print(answer)

# 문제를, 문제를 잘 읽자. 제발!!