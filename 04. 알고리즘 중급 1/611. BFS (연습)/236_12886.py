'''
문제
오늘 강호는 돌을 이용해 재미있는 게임을 하려고 한다.
먼저, 돌은 세 개의 그룹으로 나누어져 있으며 각각의 그룹에는 돌이 A, B, C개가 있다.
강호는 모든 그룹에 있는 돌의 개수를 같게 만들려고 한다.

강호는 돌을 단계별로 움직이며, 각 단계는 다음과 같이 이루어져 있다.

크기가 같지 않은 두 그룹을 고른다. 그 다음, 돌의 개수가 작은 쪽을 X, 큰 쪽을 Y라고 정한다.
그 다음, X에 있는 돌의 개수를 X+X개로, Y에 있는 돌의 개수를 Y-X개로 만든다.

A, B, C가 주어졌을 때, 강호가 돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 주어진다. (1 ≤ A, B, C ≤ 500)

출력
돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력한다.

예제 입력 1 
10 15 35
예제 출력 1 
1
예제 입력 2 
1 1 2
예제 출력 2 
0
'''

# 돌의 총합은 변하지 않는다.
# 마지막에 3X가 되어야 하니까, 애초에 입력된 총합이 3배수가 아니면 잘라버리자.

import sys
input = sys.stdin.readline

from collections import deque

A, B, C = map(int, input().split())

# 요소를 넣으면 정렬된 튜플로 반환하는 함수
def sorted_tuple_maker(X, Y, Z):
    return(tuple(sorted([X, Y, Z])))

def bfs():
    # 총합이 3의 배수가 아니면 바로 False를 반환
    if (A + B + C) % 3 != 0:
        return False

    # 방문 저장용 set()            
    visited = set()

    # 입력된 값들을 정렬된 튜플로 push
    # 정렬된 튜플을 사용하면 대소구분 코드가 필요 없음
    start = sorted_tuple_maker(A, B, C)
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        Anei, Bnei, Cnei = current
        # 세 그룹이 모두 같으면 조건 만족으로 종료
        if Anei == Bnei == Cnei:
            return True

        # 두 그룹을 고르는 세 가지 경우. 방문되지 않은 조합이면 push
        if Anei != Bnei:
            next_current = sorted_tuple_maker(Anei * 2, Bnei - Anei, Cnei)
            if next_current not in visited:
                visited.add(next_current)
                queue.append(next_current)

        if Bnei != Cnei:
            next_current = sorted_tuple_maker(Anei, Bnei * 2, Cnei - Bnei)
            if next_current not in visited:
                visited.add(next_current)
                queue.append(next_current)
        
        if Anei != Cnei:
            next_current = sorted_tuple_maker(Anei * 2, Bnei, Cnei - Anei)
            if next_current not in visited:
                visited.add(next_current)
                queue.append(next_current)

    # 모든 조합을 방문해도 조건이 만족되지 않았다면 False 반환
    return False
    
# 조건을 만족할 경우 1, 그렇지 않으면 0 출력
print(1 if bfs() else 0)

        



