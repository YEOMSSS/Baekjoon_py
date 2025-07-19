'''
문제
남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다.
그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에,
김지민은 K개의 글자를 가르칠 시간 밖에 없다.
김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다.
김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.

남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다.
남극언어에 단어는 N개 밖에 없다고 가정한다.
학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N과 K가 주어진다.
N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다.
둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다.
단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다.
모든 단어는 중복되지 않는다.

출력
첫째 줄에 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값을 출력한다.

예제 입력 1 
3 6
antarctica
antahellotica
antacartica
예제 출력 1 
2
예제 입력 2 
2 3
antaxxxxxxxtica
antarctica
예제 출력 2 
0
예제 입력 3 
9 8
antabtica
antaxtica
antadtica
antaetica
antaftica
antagtica
antahtica
antajtica
antaktica
예제 출력 3 
3
'''
# anta + tica 에는 5개가 있다. 기본 5개는 되어야 읽을 수 있음.
# 비트마스크로 풀면 되지 않을까? 주제에 맞춰서..
'''
import sys
input = sys.stdin.readline
from itertools import combinations

# 앞뒤로 4개씩 제외해서 저장하기
N, K = map(int, input().split())
words = [input().rstrip()[4 : -4] for _ in range(N)]
if K < 5:
    print(0)
    sys.exit(0)

base_chars = set(["a", "n", "t", "i", "c"])
used_chars = set()

for word in words:
    for char in word:
        if char not in base_chars:
            used_chars.add(char)

combs = combinations(used_chars, K - 5)

result = 0
for comb in combs:
    known = base_chars.union(comb)
    completed_count = 0
    for word in words:
        if all(char in known for char in word):
            completed_count += 1
    result = max(result, completed_count)

print(result)
'''
# 일단 일반적으로 그냥 풀어보는데.. 시간초과.
# 비트마스크로 ㄱㄱ

import sys
input = sys.stdin.readline
from itertools import combinations

# 앞뒤로 4개씩 제외해서 저장하기
N, K = map(int, input().split())
words = [input().rstrip()[4 : -4] for _ in range(N)]
if K < 5:
    print(0)
    sys.exit(0)

# 필수 알파벳 set집합으로 저장 후 마스크로 변환
base_chars = {"a", "n", "t", "i", "c"}
base_mask = 0
for char in base_chars:
    base_mask |= 1 << (ord(char) - ord("a"))

# 앞뒤 잘라낸 단어들을 마스크로 변환, 사용한 알파벳은 ord로 저장해두기
word_masks = [] # 단어가 중복으로 들어올 수 있으니, set사용금지
used_chars_asc = set()
for word in words:
    mask = 0
    for char in word:
        if char not in base_chars:
            char_ord = ord(char) - ord("a")
            mask |= 1 << char_ord
            used_chars_asc.add(char_ord)
    word_masks.append(mask)

# 배워야 할 총 알파벳수만큼 가르치거나, 더 많이 가르칠 수 있다면 모든 단어가 가능
if len(used_chars_asc) <= K - 5:
    print(N)
    sys.exit(0)

# 가능한 문자 조합에서 최댓값 찾기
max_count = 0
for comb in combinations(used_chars_asc, K - 5):
    # base마스크 + comb마스크
    learned_mask = base_mask
    for char_ord in comb:
        learned_mask |= 1 << char_ord

    # 이번 조합에 배운 알파벳들로 만들어지면 카운트
    completed_count = 0
    for word_mask in word_masks:
        if word_mask & ~learned_mask == 0:
            completed_count += 1

    # 최댓값 갱신
    max_count = max(max_count, completed_count)

print(max_count)

# 굳이 재귀로 안 해도, 가지치기 할만한건 다 되어있다.