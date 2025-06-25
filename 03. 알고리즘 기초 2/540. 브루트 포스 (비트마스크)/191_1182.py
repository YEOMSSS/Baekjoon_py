'''
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
'''
# 일단 생각나는대로.
'''
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in range(1, N + 1):
    combs = combinations(nums, i)
    for comb in combs:
        if sum(comb) == S:
            answer += 1

print(answer)
'''
# 너무 쉽게 맞았는데?
# 비트마스킹으로..
# mask는 "여러 비트가 모여 있는 비트열"

N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
# 1부터 2^N - 1까지 모든 부분집합 순회. 공집합 제외
# 숫자마다 01스위치가 있다고 생각하고, 사용하거나 안하거나 2가지밖에 없으니까.
# 2진수로 나타내면 모든 부분수열의 스위치 조합이 만들어질 것이다.
for mask in range(1, 1 << N):
    subset_sum = 0
    for i in range(N): # 각 자리마다 스위치 켜져있는지 확인
        if mask & (1 << i):  # 스위치 켜져있으면 sum에 추가
            subset_sum += nums[i]
    if subset_sum == S:
        answer += 1
        # print(bin(bit))

print(answer)


