'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A
'''

# string = input().upper() # 괄호를 빼먹지 마!
# alphabet = ""
# max_cnt = 0

# for char in set(string):
#     cnt = string.count(char)
#     if max_cnt < cnt:
#         max_cnt = cnt
#         alphabet = char
#     elif max_cnt == cnt:
#         alphabet = "?"

# print(alphabet)

# string.count()가 계속 반복된다. 느리다는 거지.

string = input().upper()
cnt_list = [0] * 26

for char in string:
    cnt_list[ord(char) - ord("A")] += 1
# 리스트에 알파벳이 나온 횟수가 들어간다.
max_cnt = max(cnt_list) # 리스트에서 가장 큰 숫자
if cnt_list.count(max_cnt) > 1: # 가장 큰 숫자가 두번 이상 나왔어?
    print("?") # 그럼 가장 큰게 겹치는거지, 뭐.
else:
    print(chr(cnt_list.index(max_cnt) + ord('A')))
# 안겹치면 리스트에서 가장 큰 숫자의 인덱스를 뽑아서 ord(A)에 더한 후 다시 chr()로 변환한다.
