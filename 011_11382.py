'''
문제
꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

입력
첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 10^12)이 공백을 사이에 두고 주어진다.

출력
A+B+C의 값을 출력한다.

예제 입력 1 
77 77 7777
예제 출력 1 
7931
'''

# int1, int2, int3 = map(int, input().split())

# if all(1 <= val <= 10**12 for val in (int1, int2, int3)):
#     print(int1 + int2 + int3)
# else:
#     print("올바른 수를 입력하세요.")

print(sum(map(int, input().split()))) #세상에는 sum이 존재한다.