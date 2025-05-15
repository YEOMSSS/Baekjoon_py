'''
문제
한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽),
문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.

L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때,
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오.
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

입력
첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다.
이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다.
둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다.
셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

출력
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
'''
'''
예제 입력 1 
abcd
3
P x
L
P y
예제 출력 1 
abcdyx
예제 입력 2 
abc
9
L
L
L
L
L
P x
L
B
P y
예제 출력 2 
yxabc
예제 입력 3 
dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z
예제 출력 3 
yxz
'''

# 시간제한은 300ms.

# 커서의 위치는 왼쪽 숫자의 인덱스로 한다.
# 왼쪽 끝일 때는 -1, 오른쪽 끝일 때는 len -1.
'''
import sys
input = sys.stdin.readline

answers = list(input().strip()) # abcd를 받으면 [a b c d]로 저장

cursor = len(answers) - 1 # 가장 오른쪽에서 시작

cnt = int(input().strip())

for _ in range(cnt):
    cmd = input().strip().split()

    if cmd[0] == "L":
        if cursor > -1: # 커서가 제일 왼쪽이 아니면
            cursor -= 1 # 커서를 한칸 왼쪽으로
    elif cmd[0] == "D":
        if cursor < len(answers) - 1: # 커서가 제일 오른쪽이 아니면
            cursor += 1 # 커서를 한칸 오른쪽으로
    elif cmd[0] == "B":
        if cursor > -1: # 커서가 제일 왼쪽이 아니면
            answers.pop(cursor) # 커서 왼쪽을 지우고
            cursor -= 1 # 하나 지워졌으니 커서를 한칸 왼쪽으로
    elif cmd[0] == "P":
        answers.insert(cursor + 1, cmd[1]) # 커서가 -1일때 0자리에 추가될 수 있도록 +1을 한다.
        cursor += 1 # 하나 추가됐으니 커서를 한칸 오른쪽으로

print(*answers, sep= "")
'''
# pop 이랑 insert 안에 인덱스가 들어가는 순간 시간복잡도는 떡상한다.
# 데크를 사용해보자. from collections import deque !
# 이번에 사용할 아이디어는 커서 기준으로 데크를 좌우로 나누는 것이다.

from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().strip()) # 초기 문자열 오른쪽 끝에 커서.
right = deque() # 커서의 오른쪽. right의 왼쪽 끝에 커서.

cnt = int(input()) # int()가 공백을 처리한다.
for _ in range(cnt):
    cmd = input().split() # split()이 공백을 처리한다.
    if cmd[0] == "L":
        if left: # left가 비어있지 않다면
           right.appendleft(left.pop()) # left의 top을 꺼내서 right의의 bot에 넣기
    elif cmd[0] == "D":
        if right: 
            left.append(right.popleft()) # right의 bot을 꺼내서 left의 top에 넣기
    elif cmd[0] == "B":
        if left: # left가 비어있지 않다면
            left.pop() # left의 top을 제거
    elif cmd[0] == "P":
        left.append(cmd[1]) # left의 top에 추가

print("".join(left + right)) # 두 deque를 더하고 "".join으로 출력

# 200ms대로 좀 아슬하긴 한데.. 그래도 더 최적화하기 어렵네.