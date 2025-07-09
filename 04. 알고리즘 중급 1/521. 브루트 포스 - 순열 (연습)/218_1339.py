'''
문제
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다.
이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다.
같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때,
A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면,
두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다.
둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다.
단어는 알파벳 대문자로만 이루어져있다.
모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다.
서로 다른 문자는 서로 다른 숫자를 나타낸다.

출력
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.

예제 입력 1 
2
AAA
AAA
예제 출력 1 
1998
예제 입력 2 
2
GCF
ACDEB
예제 출력 2 
99437
예제 입력 3 
10
A
B
C
D
E
F
G
H
I
J
예제 출력 3 
45
'''
# 순열로 만들어야 한다. 0~9으로 순열을 만든다.
# 근데 일단 최고자리에는 9를 고정해서 넣고 돌려도 되지 않겠나?

# 위 같은 생각으로 했다간 한참 걸렸을 거다.
# 같은 수가 높은 자릿수로 얼마나 많이 나왔는지를 저장할 방법이 있을까?

# 높은 자릿수일수록 높은 수여야 하니까, 자릿수 가중치를 만들어 보자.
# 100의자리로 등장하면 100을 저장하고, 이후 10의자리로 다시 등장하면 10을 또 더해주자.

import sys
input = sys.stdin.readline

N = int(input())

words_list = [] # 단어를 입력받을 list
visited_dict = {} # 가중치가 저장될 dict
for _ in range(N):
    word = input().rstrip()
    words_list.append(word)
    # 자릿수 가중치 구하기. 높은자릿수로 많이 등장할수록 클 것
    for idx, char in enumerate(word[::-1]):
        if char in visited_dict: # 중복되지 않게.
            visited_dict[char] += 10 ** idx
        else:
            visited_dict[char] = 10 ** idx

# dict를 items()로 list로 바꾼 후, dict의 value인 가중치 순으로 내림차순 정렬
visited_dict = sorted(visited_dict.items(), key= lambda x: x[1], reverse= True)

num_dict = {} # char를 대응하는 수와 묶어줄 dict
for idx, char in enumerate(visited_dict):
    num_dict[char[0]] = str(9 - idx) # 가중치는 사용 안하니까 [0]

result = 0
for word in words_list:
    num = ""
    for char in word:
        num += num_dict[char]
    result += int(num)

print(result)

# 218_1339의 브루트 포스 버전
# 시간최적화를 하려면 결국 그리디 아이디어가 포함되어야 하는데,
# 그러느니 그냥 그리디로 풀고 말지.

'''
from itertools import permutations

import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

letters = set()
for word in words:
    for char in word:
        letters.add(char)

letters = list(letters)
max_sum = 0

for perm in permutations(range(10), len(letters)):
    letter_to_digit = dict(zip(letters, perm))
    
    invalid = False
    for word in words:
        if len(word) > 1 and letter_to_digit[word[0]] == 0:
            invalid = True
            break
    if invalid:
        continue

    total = 0
    for word in words:
        num = ""
        for char in word:
            num += str(letter_to_digit[char])
        total += int(num)
        

    max_sum = max(max_sum, total)

print(max_sum)
'''