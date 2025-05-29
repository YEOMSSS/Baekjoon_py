'''
문제
N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.

예를 들어, N, M이 각각 0, 10일 때 0을 세면 0에 하나, 10에 하나가 있으므로 답은 2이다.

입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 줄에는 N과 M이 주어진다.

1 ≤ T ≤ 20
0 ≤ N ≤ M ≤ 1,000,000
출력
각각의 테스트 케이스마다 N부터 M까지의 0의 개수를 출력한다.

예제 입력 1 
3
0 10
33 1005
1 4
예제 출력 1 
2
199
0
'''
# 시간제한 3초면 이따위로 짜도 되지 않을까

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    answer = 0
    N, M = map(int, input().split())
    for i in range(N, M + 1):
        i = str(i)
        if "0" in i:
            answer += i.count("0")
    print(answer)

# 1880ms zzzzzzzzzzzz
# 밑에 코드는 모르겠다, GPT한테 물어봐서 이해좀 하자
'''
import sys

input = sys.stdin.readline

def solution():

    def count(n):
        if n < 0:
            return 0
        cnt = prev = 1
        i = 10
        while i <= n:
            if (n%i)//prev == 0:
                cnt += ((n-i)//i)*prev+n%prev+1
            else:
                cnt += (n//i)*prev
            prev = i
            i *= 10
        return cnt

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(count(M)-count(N-1))

solution()
'''