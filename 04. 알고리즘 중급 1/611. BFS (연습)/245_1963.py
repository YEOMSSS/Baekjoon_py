'''
문제
소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다.
어느 날 창영이는 친한 친구와 대화를 나누었는데:

“이제 슬슬 비번 바꿀 때도 됐잖아”
“응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
“그럼 8179로 해”
“흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야.
예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아.
여러 단계를 거쳐야 만들 수 있을 것 같은데... 예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
“흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래.
네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
“귀찮아”
그렇다. 그래서 여러분이 이 문제를 풀게 되었다.
입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자.
주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고,
‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

입력
첫 줄에 test case의 수 T가 주어진다. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어진다.

출력
각 test case에 대해 두 소수 사이의 변환에 필요한 최소 회수를 출력한다. 불가능한 경우 Impossible을 출력한다.

예제 입력 1 
3
1033 8179
1373 8017
1033 1033
예제 출력 1 
6
7
0
'''

# 에라토스테네스의 체를 이용해서 일단 소수판정표를 짜두자.

# 그리고 순회가 돌 때마다, 자리마다 0~9까지 다 돌려보자.
# 그리고 소수가 맞다면 push하자.

import math

import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited[int(start)] = True

    distance = 0
    while queue:

        for _ in range(len(queue)):
            current = queue.popleft()

            # 도착 시 종료
            if current == end:
                print(distance)
                return

            # 4 자릿수에 대해 각각 반복
            for i in range(4):
                # 자릿수에 맞춰 10의 제곱수를 만들어 준다.
                digits = (10 ** (3 - i))
                # current에서 현재 자릿수를 0으로 만들어 준다.
                temp = int(current) - (int(current[i]) * digits)
                # 0~9까지 전부 자리에 집어넣어 소수 판정
                for j in range(10):
                    # 천의자리가 0이 되지 않도록 한다.
                    if i == 0 and j == 0:
                        continue
                    # 비워둔 자릿수에 j를 채워넣는다.
                    neighbor = temp + (j * digits)

                    # 소수 판정
                    if not prime_list[neighbor]:
                        continue
                    # 방문 판정
                    if visited[neighbor]:
                        continue

                    queue.append(str(neighbor))
                    visited[neighbor] = True

        distance += 1

    print("Impossible")
    return

# 체로 0 ~ 9999까지 소수판정여부가 저장된 리스트를 만든다.
MAX = 9999
prime_list = [True for i in range(MAX + 1)]
prime_list[1] = False

for i in range(2, math.isqrt(MAX) + 1):
    if prime_list[i] == True:
        j = 2
        while i * j <= MAX:
            prime_list[i * j] = False
            j += 1

T = int(input())

for _ in range(T):
    A, B = input().split()

    visited = [False] * 10000
    bfs(A, B)

# 쉽게 풀었네.