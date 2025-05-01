'''
문제
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력
첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다.
또한 문자열은 공백으로 시작하거나 끝날 수 있다.

출력
첫째 줄에 단어의 개수를 출력한다.

예제 입력 1 
The Curious Case of Benjamin Button
예제 출력 1 
6
예제 입력 2 
 The first character is a blank
예제 출력 2 
6
예제 입력 3 
The last character is a blank 
예제 출력 3 
6
'''

# 처음에 쓴 코드

'''
sentence = input()

word_count = sentence.count(" ") + 1

# if sentence[0] == " " or sentence[-1] == " ":
#     word_count -= 1   # 이렇게 or를 쓰면 앞뒤가 다 " "일때가 망가진다.

if sentence[0] == " ":
    word_count -= 1
if sentence[-1] == " ":
    word_count -= 1

print(word_count)

# 그리고 이러면 공백이 들어올 때 에러가 난다.
# [0]이랄 게 존재하지 않기 때문.
'''

# 두번째로 쓴 코드

'''
# s = input().strip()
# strip으로 공백을 없애는 방법도 있다.

sentence = input().strip()
print(sentence.count(" ") + 1)

# 근데 이러면 아무것도 입력되지 않았을 때 1이 반환된다.
# 때문에 공백일 경우 0을 따로 반환해야 하기에 귀찮다.
'''

# split까지 사용해 보자.

sentence = input().strip().split()
print(len(sentence))

# sentence는 리스트가 된다.
# len([]) == 0이다.

