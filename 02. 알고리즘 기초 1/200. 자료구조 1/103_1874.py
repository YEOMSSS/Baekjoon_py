'''
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아
제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다.
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
'''
'''
예제 입력 1 
8
4
3
6
8
7
5
2
1
예제 출력 1 
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
예제 입력 2 
5
1
2
5
3
4
예제 출력 2 
NO
힌트
1부터 n까지에 수에 대해 차례로
[push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop]
연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
'''
# 문제를 ㅈ같이 써놨네... 괜찮은 것 같기도 하고? 그냥 처음보면 조금 헷갈릴 수 있는 정도.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 1부터 n까지 수열에 push로 넣고, pop으로 꺼낸다.
# pop으로 꺼내면 원래 수열에서 하나 없어지고 그게 답 수열에 append된다.
# 위에 힌트를 보면 push 4번 해서 [1, 2, 3, 4] 만들고 첫 pop으로 4 꺼내고 둘째 pop으로 3 꺼낸다.
# 그리고 다시 push 2번 해주면 [1, 2, 5, 6]이랑 답 수열 [4, 3]이 되는 것.
# pop push push 하면 1 2 5 7 8, 4 3 6
# pop 5번 하면 4 3 6 8 7 5 2 1 이 되는 것이다. 이해했지?

from collections import deque
import sys
input = sys.stdin.readline

cnt = int(input().strip())
target_list = deque([int(input().strip()) for _ in range(cnt)])

num_list = [0]
# ans_list = []
output = []

minus_count = 0
for i in range(1, cnt + 1):
    num_list.append(i)
    output.append("+")
    while target_list[0] == num_list[-1]:
        num_list.pop()
        # ans_list.append(num_list.pop()) 필요 없었네 이거?
        output.append("-")
        minus_count += 1
        if minus_count == cnt:
            break
        target_list.popleft() # popleft()를 쓰기 위해 deque까지 사용했다

if minus_count == cnt:
    print("\n".join(output))
else:
    print("NO")

# 빡세다 빡세.. 복습은 내일하자