'''
문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

예제 입력 1 
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
예제 출력 1 
NO
NO
YES
NO
YES
NO
예제 입력 2 
3
((
))
())(()
예제 출력 2 
NO
NO
NO
'''
# 생각을 해보자.
# (로 시작해서 )로 끝나고, (와 )의 개수가 같다면 성립하겠지?
'''
cnt = int(input())

for _ in range(cnt):
    PS = input()
    if PS[0] == "(" and PS[-1] == ")" and PS.count("(") == PS.count(")"):
        print("YES")
    else:
        print("NO")
'''
# 아니!! ())(()는 VPS가 아니야!! 올바르지 않다고. 하지만 YES가 나와버려.
# 어떻게 해결해야 하지? 대체?
# 맨 앞에서부터 (, )를 하나씩 세다가 )이 (보다 많아지면 VPS가 아니야!!
'''
cnt = int(input())

for _ in range(cnt):
    open_cnt = 0 # 이게 반복문 안에 있어야 초기화가 되지
    close_cnt = 0 # 반복문 밖에 있으면 이전 시행이 누적된다고.
    string = input()
    if string[0] == "(" and string[-1] == ")" and string.count("(") == string.count(")"):
        for char in string: # 위 조건 만족한 상태에서 ) 이 ( 보다 많아지면 NO
            if char == "(":
                open_cnt += 1
            elif char == ")":
                close_cnt += 1
            if open_cnt < close_cnt:
                print("NO") # NO 출력하고 break
                break
        else:
            print("YES") # break 없이 다 돌면 YES
    else: # 아예 처음부터 조건만족 안되면 NO
        print("NO")
'''
# 조금 더 최적화할 수 있을까? 굳이 open, close 둘 다 써야해?
# open이면 1 더하고 close면 1 빼. 음수가 되는 순간 close가 넘어간거지.
# 또, 첫 조건에서 개수 비교를 하잖아? 이건 둘의 합이 0인지 보면 되고.
# 처음과 끝이 ()인지 확인하는 건 이 과정에선 필요 없겠어. 끝이 )가 아니면 음수가 되어버리니까.
'''
cnt = int(input())

for _ in range(cnt):
    balance = 0
    string = input()
    for char in string: # 위 조건 만족한 상태에서 ) 이 ( 보다 많아지면 NO
        balance += 1 if char == "(" else -1 # 아래 네 줄을 한줄로.
        # if char == "(":
        #     balance += 1
        # else: # ")"일 때
        #     balance -= 1
        if balance < 0:
            print("NO") # NO 출력하고 break
            break
    else:
        print("YES" if balance == 0 else "NO") # ()개수 같은지 확인. 만약 아니면 NO 출력
'''
# readline도 써야지.
# cnt도 쓰지 말자. 귀찮다.

import sys
input = sys.stdin.readline

for _ in range(int(input().strip())): # \n까지 받아오면 ㅈ될수있으니 앞뒤 공백 제거
    balance = 0
    string = input().strip()
    for char in string: # 위 조건 만족한 상태에서 ) 이 ( 보다 많아지면 NO
        balance += 1 if char == "(" else -1 # 아래 네 줄을 한줄로.
        # if char == "(":
        #     balance += 1
        # else: # ")"일 때
        #     balance -= 1
        if balance < 0:
            print("NO") # NO 출력하고 break
            break
    else:
        print("YES" if balance == 0 else "NO") # ()개수 같은지 확인. 만약 아니면 NO 출력