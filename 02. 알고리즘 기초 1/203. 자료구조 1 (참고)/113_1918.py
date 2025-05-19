'''
문제
수식은 일반적으로 3가지 표기법으로 표현할 수 있다.
연산자가 피연산자 가운데 위치하는 중위 표기법(일반적으로 우리가 쓰는 방법이다),
연산자가 피연산자 앞에 위치하는 전위 표기법(prefix notation),
연산자가 피연산자 뒤에 위치하는 후위 표기법(postfix notation)이 그것이다.
예를 들어 중위 표기법으로 표현된 a+b는 전위 표기법으로는 +ab이고, 후위 표기법으로는 ab+가 된다.

이 문제에서 우리가 다룰 표기법은 후위 표기법이다.
후위 표기법은 위에서 말한 법과 같이 연산자가 피연산자 뒤에 위치하는 방법이다. 이 방법의 장점은 다음과 같다.
우리가 흔히 쓰는 중위 표기식 같은 경우에는 덧셈과 곱셈의 우선순위에 차이가 있어 왼쪽부터 차례로 계산할 수 없지만
후위 표기식을 사용하면 순서를 적절히 조절하여 순서를 정해줄 수 있다.
또한 같은 방법으로 괄호 등도 필요 없게 된다. 예를 들어 a+b*c를 후위 표기식으로 바꾸면 abc*+가 된다.

중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다.
우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다.
그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다.
그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다.
마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

다른 예를 들어 그림으로 표현하면 A+B*C-D/E를 완전하게 괄호로 묶고 연산자를 이동시킬 장소를 표시하면 다음과 같이 된다.

결과: ABC*+DE/-

이러한 사실을 알고 중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오

입력
첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다.
그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다.
표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다. 

출력
첫째 줄에 후위 표기식으로 바뀐 식을 출력하시오

예제 입력 1 
A*(B+C)
예제 출력 1 
ABC+*
예제 입력 2 
A+B
예제 출력 2 
AB+
예제 입력 3 
A+B*C
예제 출력 3 
ABC*+
예제 입력 4 
A+B*C-D/E
예제 출력 4 
ABC*+DE/-
'''
# */ 가 나오면 바로 오른쪽으로 넘기고
# +- 가 나오면 */ 를 건너뛰어 오른쪽으로 넘긴다.
# 알파벳이 나오면 기호를 오른쪽으로 넘긴다.
# +-가 나오기 전까지 기호를 넘기면 되겠네. 이거구만?
# 근데 괄호가 있으면 그 안에서 일단 먼저 넘겨주고.
# 괄호 안 계산하고, */넘기고, +-넘기면 되겠다.
'''
import sys
input = sys.stdin.readline

from collections import deque

string = list(input().strip())

answer = []
stack = []

for char in string:
    match char:
        case "+" | "-":
            if stack and stack[-1] == "(":
                stack.append(char)
                continue
            while stack:
                answer.append(stack.pop())
            stack.append(char)
        case "*" | "/":
            if stack and stack[-1] == "(":
                stack.append(char)
                continue
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer.append(stack.pop())
            stack.append(char)
        case "(":
            stack.append(char)
        case ")":
            while stack and stack[-1] != "(":
                answer.append(stack.pop())
            stack.pop()
        case _:
            answer.append(char)
answer = answer + list(stack)[::-1]

print("".join(answer))
'''
# 런타임 에러?? 최적화하자.. 그리고 오류가 있다고? 흠..

import sys
input = sys.stdin.readline

string = list(input().strip())

answer = []
stack = []

priority = {"+": 1, "-": 1, "*": 2, "/": 2} # 연산자 우선순위 정의

for char in string:
    if char.isalpha():  # 알파벳이면 그대로 출력
        answer.append(char)
    elif char == "(":
        stack.append(char)
    elif char == ")":
        while stack and stack[-1] != '(':
            answer.append(stack.pop()) # 괄호 내부 연산 마무리. 마지막에 하는거랑 똑같은거거
        stack.pop()  # ( 삭제
    else:  # +-*/의 경우 char in priority
        while stack and stack[-1] != "(" and priority.get(stack[-1], 0) >= priority[char]:
        # 스택의 top이 (가 아니면서 우선순위가 char보다 같거나 높을 때
            answer.append(stack.pop())
        stack.append(char)
        # (거나 우선순위가 더 높으면 stack에 push

# 남은 연산자 모두 출력
while stack:
    answer.append(stack.pop()) # 리스트 뒤집기보다 이렇게 하는게 좋대.

print("".join(answer))
