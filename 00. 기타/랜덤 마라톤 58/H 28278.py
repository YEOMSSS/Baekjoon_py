'''
1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    command = list(map(int, input().split()))

    match command[0]:
        case 1:
            stack.append(command[1])
        case 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        case 3:
            print(len(stack))
        case 4:
            if stack:
                print(0)
            else:
                print(1)
        case 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)



