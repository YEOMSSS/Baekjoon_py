'''
문제
정수 s가 주어진다. 정수 s의 값을 t로 바꾸는 최소 연산 횟수를 구하는 프로그램을 작성하시오.

사용할 수 있는 연산은 아래와 같다.

s = s + s; (출력: +)
s = s - s; (출력: -)
s = s * s; (출력: *)
s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)
입력
첫째 줄에 s와 t가 주어진다. (1 ≤ s, t ≤ 109)

출력
첫째 줄에 정수 s를 t로 바꾸는 방법을 출력한다.
s와 t가 같은 경우에는 0을, 바꿀 수 없는 경우에는 -1을 출력한다.
가능한 방법이 여러 가지라면, 사전 순으로 앞서는 것을 출력한다. 

연산의 아스키 코드 순서는 '*', '+', '-', '/' 이다.

예제 입력 1 
7 392
예제 출력 1 
+*+
예제 입력 2 
7 256
예제 출력 2 
/+***
예제 입력 3 
4 256
예제 출력 3 
**
예제 입력 4 
7 7
예제 출력 4 
0
예제 입력 5 
7 9
예제 출력 5 
-1
예제 입력 6 
10 1
예제 출력 6 
/
'''

import sys
input = sys.stdin.readline

from collections import deque

S, T = map(int, input().split())

visited = set()

def bfs(start, goal):
    if start == goal:
        return 0

    queue = deque()
    queue.append((start, 0))
    visited.add(start)

    distance = 0

    while queue:
        for _ in range(len(queue)):
            current, signal = queue.popleft()

            if current == goal:
                return signal

            # 1:*, 2:+, 3:-, 4:/
            temp = [current ** 2, current * 2, 0, 1]
            for i, neighbor in enumerate(temp):

                if neighbor > goal:
                    continue
                if neighbor in visited:
                    continue
                
                queue.append((neighbor, signal + ((i + 1) * (10 ** distance))))
                visited.add(neighbor)

        distance += 1

    return -1

result = bfs(S, T)

if result == 0 or result == -1:
    print(result)
else:
    for sig in str(result)[::-1]:
        if sig == "1":
            print("*", end= "")
        elif sig == "2":
            print("+", end= "")
        elif sig == "3":
            print("-", end= "")
        elif sig == "4":
            print("/", end= "")

# 아 염병, 입력범위가 10의 9승이었네
# 그거 말고는 쉽게 풀었다.

# 길고 긴 611단계를 끝냈구나. 고생 안 했다. 더 열심히 했어야지.
# 네가 무슨 짓을 해도 단백질을 날라주는 세포를 위해서...