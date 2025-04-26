'''
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.

예제 입력 1 
3
예제 출력 1 
611
'''

def calc_sum(count):
    sum = 0
    for i in range(1, count + 1):
        sum += i
    return sum

count = int(input())

if 1 <= count <= 10000:
    print(calc_sum(count))
else:
    print("올바른 수를 입력하세요.")

# n = int(input())
# print((n+1)*n//2)
# 반복문 안쓰는 방법. 뭔지 알지?