'''
문제
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다.
카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.
블랙잭은 카지노마다 다양한 규정이 있다.

한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다.
그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다.
블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

예제 입력 1 
5 21
5 6 7 8 9
예제 출력 1 
21
예제 입력 2 
10 500
93 181 245 214 315 36 185 138 216 295
예제 출력 2 
497
'''
'''
# 주제가 브루트 포스인만큼, 사용해 보자.
# 뭐? 이름만 멋있지 무식하게 때려넣는 노가다라고?

N_cnt, M_sum = map(int, input().split())
cards = list(map(int, input().split()))

sum_max = 0
for i in range(len(cards)):
    i_val = cards.pop(i)
    for j in range(len(cards) - 1):
        j_val = cards.pop(j)
        for k in range(len(cards) - 2):
            if sum_max < i_val + j_val + cards[k] <= M_sum:
                sum_max = i_val + j_val + cards[k]
        cards.insert(j, j_val)
    cards.insert(i, i_val)

print(sum_max)

# 뭔가 안될거같긴 한디.
'''
# 코드의 아이디어는 좋지만, list.pop(i)와 list.insert(i, x)를 반복해서 쓰는 방식은 문제가 있습니다.
# 특히 리스트를 수정하면서 반복문을 돌리면 인덱스가 꼬일 수 있고, pop을 하면 리스트 크기도 바뀌기 때문입니다.
# → 즉, 이 코드는 인덱스 오류나 논리 오류를 유발할 가능성이 높습니다.
# GPT 형님이 그러시댄다.
'''
N_cnt, M_sum = map(int, input().split())
cards = list(map(int, input().split()))

sum_max = 0
for i in range(N_cnt):
# 카드가 5장이라 하면, 일단 첫 카드부터 픽하고 0 1 2 3(x) 4(x)
    for j in range(i + 1, N_cnt):
    # 첫 카드 다음 카드부터 픽하고 01 02 03 04(x) 12 13 14(x) 23 24(x)
        for k in range(j + 1, N_cnt):
        # 다음 카드의 다음 카드부터 픽한다. 012 013 014 023 024 034 123 124 134 234
            total = cards[i] + cards[j] + cards[k]
            if sum_max < total <= M_sum:
                sum_max = total

print(sum_max)
'''
# 그런데 사실 itertools 에서 combinations를 import하면 정말 쉬워지는데

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

sum_max = 0
for combo_3 in combinations(cards, 3):
# cards 리스트에서 서로 다른 3장의 카드를 고르는 모든 조합을 튜플로 생성한다
    total = sum(combo_3)
    if sum_max < total <= M:
        sum_max = total

print(sum_max)


