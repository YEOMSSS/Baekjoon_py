'''
문제
N개의 에너지 구슬이 일렬로 놓여져 있고, 에너지 구슬을 이용해서 에너지를 모으려고 한다.

i번째 에너지 구슬의 무게는 Wi이고, 에너지를 모으는 방법은 다음과 같으며, 반복해서 사용할 수 있다.

에너지 구슬 하나를 고른다. 고른 에너지 구슬의 번호를 x라고 한다.
단, 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
x번째 에너지 구슬을 제거한다.
Wx-1 × Wx+1의 에너지를 모을 수 있다.
N을 1 감소시키고, 에너지 구슬을 1번부터 N번까지로 다시 번호를 매긴다.
번호는 첫 구슬이 1번, 다음 구슬이 2번, ... 과 같이 매겨야 한다.
N과 에너지 구슬의 무게가 주어졌을 때, 모을 수 있는 에너지 양의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 에너지 구슬의 개수 N(3 ≤ N ≤ 10)이 주어진다.

둘째 줄에는 에너지 구슬의 무게 W1, W2, ..., WN을 공백으로 구분해 주어진다. (1 ≤ Wi ≤ 1,000)

출력
첫째 줄에 모을 수 있는 에너지의 최댓값을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
12
예제 입력 2 
5
100 2 1 3 100
예제 출력 2 
10400
예제 입력 3 
7
2 2 7 6 90 5 9
예제 출력 3 
1818
예제 입력 4 
10
1 1 1 1 1 1 1 1 1 1
예제 출력 4 
8
'''

# 포문으로 idx 1 ~ idx len-2까지 돌리고
# idx pop하고 에너지 누적하고 pop한리스트 다시 재귀돌리고
# len == 2 되면 return하고 그런식으로 최댓값구하고

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

energys_list = list(map(int, input().split()))

# 최댓값 누적용
result = 0

# dfs원리로 모든 pop을 실행하며 누적합 모으기
def dfsR(e_list, acc):
    global result
    # 길이가 2가 되면 더 이상 에너지를 모을 수 없다.
    if len(e_list) == 2:
        result = max(result, acc)
        return

    # 1~idx-2 까지 전부 pop해보기
    for i in range(1, len(e_list) - 1):
        target = e_list.pop(i)
        # i-1과 i+1(pop된걸 고려해서 i로 사용)
        created_energy = e_list[i - 1] * e_list[i]
        dfsR(e_list, acc + created_energy)
        e_list.insert(i, target) # 다음 반복을 위해 원상복구

# 재귀 실행
dfsR(energys_list, 0)
print(result)

# 쉽네. 이제 실버1도 무리가 없다
