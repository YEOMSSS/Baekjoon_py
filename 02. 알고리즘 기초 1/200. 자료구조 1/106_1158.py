'''
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

출력
예제와 같이 요세푸스 순열을 출력한다.

예제 입력 1 
7 3
예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
'''
# 1 2 '3' 4 5 '6' 7    1 '2' 4 5 '7'    1 4 '5'    1 4    '1' 4    4    '4'
# 문제는 이해했다.
'''
import sys
input = sys.stdin.readline # 그냥 써. 그냥. 반복문 안에 있는게 아니더라도 일단 써!!

N, K = map(int, input().split())

peoples = list(range(1, N + 1)) # 길게 만들 리스트. 그냥 K의 배수로 인덱스를 뽑으면 답이 나오도록 할 것
temp = list(range(1, N + 1)) # 숫자 제거용 리스트. answer에 넣은 숫자는 제거할 것이다.

answers = []

cnt = 0
while len(answers) != N:
    cnt += 1
    while len(peoples) < K * cnt: # peoples의 길이가 숫자를 제거한 횟수 * K 보다 작으면
        peoples += temp # answer에 추가된 숫자가 빠진 리스트를 peoples에 붙인다.
    answers.append(peoples[K * cnt - 1]) # K의 배수 인덱스를 answers에 넣는다.
    temp.remove(answers[-1]) # answers에 넣은 수를 temp에서 제거하여 peoples에 붙일 수 있도록 준비한다.

print(f"<{', '.join(map(str, answers))}>")
'''
# 너무! 너무! 복잡해! 쓸데없어! 간단한 방법이 필요해!
# 굳이 temp를 만들고, peoples를 존나 길게 만들어야 할까?
# deque에는 rotate라는 게 있다는데?
'''
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = deque(range(1, N + 1))
answers = []

while people: # people이 다 털릴 때까지 돌린다.
    people.rotate(-(K - 1))  # K-1만큼 왼쪽으로 회전.
    # K-1번밖에 안 도는 것 같지만, 제거하는 것으로 한번 회전한 셈이 된다.
    answers.append(people.popleft())  # K번째 회전 차례에 회전 대신 삭제하는 것이다.

print(f"<{', '.join(map(str, answers))}>")
'''
# 역시 쌩쑈를 해봐야 기억에 더 잘 남는군.
# 아마 rotate는 평생 기억하지 않을까?

N, K = map(int, input().split())
people = list(range(1, N + 1))
answers = []
cnt = 0 # 제거할 사람의 인덱스.
for i in range(N):
    cnt = (cnt + K - 1) % len(people) # 어떻게 이런 식이!
    # -1은 인덱스가 0부터 시작이기 때문에 붙이는 것
    # % len(people)은 cnt가 리스트를 넘어가는 경우를 관리한다.
    answers.append((people.pop(cnt)))
print(f"<{', '.join(map(str, answers))}>")

# 이런건 대체 어떻게 생각하는거냐?