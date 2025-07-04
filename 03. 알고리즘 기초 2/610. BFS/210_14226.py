'''
문제
영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다.
이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.
모든 연산은 1초가 걸린다.
또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다.
클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다.
또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다.
화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.

출력
첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
4
예제 출력 2 
4
예제 입력 3 
6
예제 출력 3 
5
예제 입력 4 
18
예제 출력 4 
8
'''
# 단방향 그래프 느낌. 최단거리니까 bfs.
# 복붙(2배) or 하나지우기(-1) 의 이동경로만 집어넣으면 되겠다.
# 복붙은 2초 걸리고 하나지우기는 1초 걸리네.

# 복사해둔걸 그냥 붙여넣기만 하는 방법도 있구나??? ㅆㅃ!!
# 이러면 복붙을 합치면 안되고, 튜플로 거리랑 같이 클립보드를 집어넣어줘야 한다.

from collections import deque

S = int(input())

# 화면 개수, 클립보드 개수 두 상태로 구성
# visited[화면][클립보드] = 시간
visited = [[-1] * (S + 1) for _ in range(S + 1)]

queue = deque()
queue.append((1, 0))  # (화면 개수, 클립보드 개수)
visited[1][0] = 0

while queue:
    screen, clip = queue.popleft()
    # 복사: 클립보드에 화면을 넣는다
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clip] + 1
        queue.append((screen, screen))

    # 붙여넣기: 화면에 클립보드 + 화면을 넣는다
    if clip > 0 and screen + clip <= S and visited[screen + clip][clip] == -1:
        visited[screen + clip][clip] = visited[screen][clip] + 1
        queue.append((screen + clip, clip))

    # 삭제: 화면에서 1을 뺀다
    if screen > 1 and visited[screen - 1][clip] == -1:
        visited[screen - 1][clip] = visited[screen][clip] + 1
        queue.append((screen - 1, clip))

# 정답은 visited[S][*] 중 최솟값
answer = min([visited[S][i] for i in range(S + 1) if visited[S][i] != -1])
print(answer)