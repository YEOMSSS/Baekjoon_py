'''
입력
첫째 줄에 테스트 케이스의 개수 N이 주어진다. 다음 N개의 줄에는 3개의 정수 r, e, c가 주어진다.
r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용이다. (-106 ≤ r,e ≤ 106, 0 ≤ c ≤ 106)

출력
각 테스트 케이스에 대해서, 광고를 해야 하면 "advertise",
하지 않아야 하면 "do not advertise", 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

예제 입력 1 
3
0 100 70
100 130 30
-100 -70 40
예제 출력 1 
advertise
does not matter
do not advertise
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    r, e, c = map(int, input().split())

    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("do not advertise")