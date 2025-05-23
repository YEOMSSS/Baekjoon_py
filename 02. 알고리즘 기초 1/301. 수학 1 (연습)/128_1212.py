'''
문제
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

입력
첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.

출력
첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.

예제 입력 1 
314
예제 출력 1 
11001100
'''
# 일단 내장함수로 풀어보고
'''
print(bin(int(input(), 8))[2:])
'''
# 구현해보자.
# 8진수를 앞에서부터 하나씩 뜯어서 2진수 세자리로 바꿔 붙이면 된다.

num = input()

answer = []
for i in num:
    i = int(i)
    # answer.append(i // 4)
    # answer.append(i % 4 // 2)
    # answer.append(i % 2)
    answer.extend([i // 4, i % 4 // 2, i % 2])
print(int("".join(map(str, answer))))