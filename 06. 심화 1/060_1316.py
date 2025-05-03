'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다
.예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''
'''
예제 입력 1 
3
happy
new
year
예제 출력 1 
3
예제 입력 2 
4
aba
abab
abcabc
a
예제 출력 2 
1
예제 입력 3 
5
ab
aa
aca
ba
bb
예제 출력 3 
4
예제 입력 4 
2
yzyzy
zyzyz
예제 출력 4 
0
예제 입력 5 
1
z
예제 출력 5 
1
예제 입력 6 
9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz
예제 출력 6 
2
'''


# cnt = int(input())
# ans = 0

# for _ in range(cnt):
#     string = input()

#     group = ""
#     for i in range(1, len(string)):
#         if string[i - 1] != string[i]:
#             group += string[i - 1]
#     group += string[-1]
#     # 앞뒤글자가 다르면 group에 앞글자를 넣는다
#     # group은 연속된 글자가 지워진 리스트가 됨.

#     str_list = []
#     for i in range(ord("a"), ord("z") + 1):
#         str_list.append(group.count(chr(i)))
#     # group에 알파벳이 몇번씩 들어가는지 센 리스트를 생성

#     if all(val < 2 for val in str_list):
#         ans += 1
#     # 센 리스트에 2 이상이 있으면 두번 이상 끊어져 나왔다는 것.

# print(ans)
# # 나쁘지 않은 것 같은데.


cnt = int(input())
ans = 0

for _ in range(cnt):
    string = input()
    seen = [] # 지금까지 나온 알파벳 저장
    prev = "" # 바로 전 글자 저장

    for char in string:
        if char != prev: # 전 글자와 다르다면
            seen.append(char) # seen에 그 글자를 넣는다
        prev = char # 전 글자에 현 글자를 넣어 갱신한다

    if len(seen) == len(set(seen)):
        ans += 1 # 중복이 없다면 ans에 1을 더한다

print(ans)
# 훨씬 깔끔하다!