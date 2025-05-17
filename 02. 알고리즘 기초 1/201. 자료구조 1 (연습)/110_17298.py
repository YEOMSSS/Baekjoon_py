'''
문제
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

예제 입력 1 
4
3 5 2 7
예제 출력 1 
5 7 7 -1
예제 입력 2 
4
9 5 4 8
예제 출력 2 
-1 8 8 -1
'''
# with 트릭컬 리바이브 엘리아스 프론티어 대기 BGM 1시간
# 골드 입문 문제다. 잘 해보자.

# NGE(i) 는 오른쪽에 있는 자신보다 큰 수 중 가장 왼쪽에 있는 수이다.

# deque를 써서 104_1406처럼 한번 리스트를 두개로 나눠볼까?
'''
import sys
input = sys.stdin.readline

from collections import deque

cnt = int(input())

target = deque()
nums = deque(map(int, input().split()))

answers = []

for _ in range(len(nums)):
    target.append(nums.popleft())
    for num in nums:
        if target[-1] < num:
            answers.append(num)
            break
    else:
        answers.append(-1)
print(*answers)
'''
# 하 씨 왜 실버보다 쉬운거같지? 난이도 기준이 뭐지 ㅅㅂ?
# 시간초과 날 거 알고 박았으니까 이제 최적화 해보자. 지금 O(N^2)니까.
# O(N)으로 만드는 건 생각보다 어렵다. 흠...

import sys
input = sys.stdin.readline

cnt = int(input())
nums = list(map(int, input().split()))
answers = [-1] * cnt # 일단 -1을 다 넣어두자.

stack = [] # 오큰수를 찾지 못한 인덱스가 저장되는 리스트

for i in range(cnt):
    while stack and nums[stack[-1]] < nums[i]: # nums[stack의 top] 이 nums[i]보다 작으면
        answers[stack.pop()] = nums[i] # 오큰수를 찾은 인덱스를 stack에서 빼고 answers에 덮어씌운다.
    stack.append(i) # 오큰수를 찾아야 하는 인덱스를 stack에 넣는다.

print(*answers)
# 어렵다. 확실히 어렵다.
# 혼자서 그냥 떠올려 내기에는 무리가 있다. 존나 어렵다.
# 이런 식의 대가리 굴리기를 연습해야 한다.
# 괜히 골드가 아니구나 싶다. 논리는 알겠는데... 어렵다.