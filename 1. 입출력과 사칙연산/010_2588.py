'''
문제
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.



(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

예제 입력 1 
472
385
예제 출력 1 
2360
3776
1416
181720
'''

# int1 = int(input())
# int2 = input()

# list2 = [int(val) for val in int2]

# print(int1 * list2[2])
# print(int1 * list2[1])
# print(int1 * list2[0])
# print(int1 * int(int2))

int1 = int(input())
int2 = input()

for i in range (1, 4):
    print(int1 * int(int2[-i])) #리스트 안에 음수는 뒤에서부터.
print(int1 * int(int2))

