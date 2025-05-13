'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
'''
예제 입력 1 
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
예제 출력 1 
2
2
0
2
1
-1
0
1
-1
0
3
예제 입력 2 
7
pop
top
push 123
top
pop
top
pop
예제 출력 2 
-1
-1
123
123
-1
-1
'''
# 백문제 뚫어보자~~!!!

# 스택의 가장 위란 인덱스 -1 을 의미한다.
'''
def push_func(X, stack):
    stack.append(X)

def pop_func(stack):
    if not stack:
        print(-1)
    else:
        print(stack.pop(-1))

def size_func(stack):
    print(len(stack))

def empty_func(stack):
    print(1 if not stack else 0) # 한줄 코드
    # if not stack:
    #     print(1)
    # else:
    #     print(0)

def top_func(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])

cnt = int(input())

stack = []
for _ in range(cnt):
    cmd = input().split() # cmd는 리스트이다.
    if cmd[0] == "push":
        push_func(int(cmd[1]), stack)
    elif cmd[0] == "pop":
        pop_func(stack)
    elif cmd[0] == "size":
        size_func(stack)
    elif cmd[0] == "empty":
        empty_func(stack)
    elif cmd[0] == "top":
        top_func(stack)
'''
# 너무 오래 걸려~~~!!!
# GPT 형님은 readline 을 추천하시네.

import sys
input = sys.stdin.readline

def push_func(X, stack):
    stack.append(X)

def pop_func(stack):
    print(stack.pop() if stack else -1)
    # if not stack:
    #     print(-1)
    # else:
    #     print(stack.pop(-1))

def size_func(stack):
    print(len(stack))

def empty_func(stack):
    print(1 if not stack else 0) # 한줄 코드
    # if not stack:
    #     print.append(1)
    # else:
    #     print.append(0)

def top_func(stack):
    print(stack[-1] if stack else -1)
    # if not stack:
    #     print(-1)
    # else:
    #     print(stack[-1])

cnt = int(input())

stack = []
for _ in range(cnt):
    cmd = input().split() # cmd는 리스트이다.
    if cmd[0] == "push":
        push_func(int(cmd[1]), stack)
    elif cmd[0] == "pop":
        pop_func(stack)
    elif cmd[0] == "size":
        size_func(stack)
    elif cmd[0] == "empty":
        empty_func(stack)
    elif cmd[0] == "top":
        top_func(stack)

# 일단 통과는 된다. 꼭 input 말고 readline을 써야겠네.
# print, "\n".join 도 추천받았았는데 이것도 해볼까.
'''
import sys
input = sys.stdin.readline

def push_func(X, stack):
    stack.append(X)

def pop_func(stack, output):
    if not stack:
        output.append(-1)
    else:
        output.append(stack.pop(-1))

def size_func(stack, output):
    output.append(len(stack))

def empty_func(stack, output):
    output.append(1 if not stack else 0) # 한줄 코드
    # if not stack:
    #     output.append(1)
    # else:
    #     output.append(0)

def top_func(stack, output):
    if not stack:
        output.append(-1)
    else:
        output.append(stack[-1])

cnt = int(input())
stack = []
output = []

for _ in range(cnt):
    cmd = input().split() # cmd는 리스트이다.
    if cmd[0] == "push":
        push_func(int(cmd[1]), stack)
    elif cmd[0] == "pop":
        pop_func(stack, output)
    elif cmd[0] == "size":
        size_func(stack, output)
    elif cmd[0] == "empty":
        empty_func(stack, output)
    elif cmd[0] == "top":
        top_func(stack, output)

print("\n".join(map(str, output)))
'''
# print를 한번에 모아서 출력하는 join을 써봤는데...
# 시간초가 똑같다! 젠장할!

# 함수 없이 조건문에서 직접 프린트하는 방법도 있지만...
# 실상황에서 그건 큰 차이가 없네네여