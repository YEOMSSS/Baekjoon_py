'''
두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.

입력
첫째 줄에 N(4 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에 S가 주어진다.
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다.
Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

예제 입력 1 
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
예제 출력 1 
0
예제 입력 2 
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
예제 출력 2 
2
예제 입력 3 
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
예제 출력 3 
1
예제 입력 4 
5
0 3 1 1 1
3 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
예제 출력 4 
0
'''
# i, N-i로 일단 팀원 수를 정한다. 앞문제에 이게 추가된다고 생각하면 될 듯.
# 팀원수를 바탕으로 조합을 굴려 팀원을 구한다.
# 팀원을 combination(team, 2)에 집어넣어 능력치를 구한다.

import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
stat_list = [list(map(int, input().split())) for _ in range(N)]

min_gap = float("inf")
all_players = set(range(N))
team1 = [0] # 팀1이 0번을 챙기는 경우만 따지면 된다.
# 팀1에 0이 없으면 팀2에 있을거고, 두 팀을 바꾸면 똑같은 경우임.

team1_headcounts = range(1, N) # 팀1의 가능한 인원수 목록. 1~N-1

def backtrack(start, headcount):
    global min_gap

    if min_gap == 0: # 차가 0 되버리면 그냥 함수 스톱
        return
    
    if len(team1) == headcount:
        team2 = list(all_players - set(team1))

        gap1 = sum(stat_list[i][j] + stat_list[j][i] for i, j in combinations(team1, 2))
        gap2 = sum(stat_list[i][j] + stat_list[j][i] for i, j in combinations(team2, 2))
        gap = abs(gap1 - gap2)
        min_gap = min(min_gap, gap)
        return

    # 팀1을 구하는 조합
    for i in range(start, N):
        team1.append(i)
        backtrack(i + 1, headcount)
        team1.pop()

# 팀1에 가능한 모든 인원수를 다 넣어본다.
for team1_headcount in team1_headcounts:
    backtrack(1, team1_headcount)

print(min_gap)