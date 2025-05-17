'''
입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

출력
첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

예제 입력 1 
150
266
427
예제 출력 1 
3
1
0
2
0
0
0
2
0
0
'''
# 250517

import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

answers = [0] * 10

for char in str(A * B * C):
    answers[int(char)] += 1

print("\n".join(map(str, answers)))