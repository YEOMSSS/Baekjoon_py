'''
문제
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 
이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

출력
첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.

예제 입력 1 
baekjoon
예제 출력 1 
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon
'''

import sys
input = sys.stdin.readline

string = input().strip()

# for i in range(1, len(string) + 1): # 굳이 len에서 뺄 필요가 없잖아?
#     answer.append(string[len(string) - i :]) # 근데 속도는 이게 로직상 좀 더 빠르네.

# for i in range(len(string)):
#     answer.append(string[i:]) # 한줄로 써도 될 것 같은데.

answer = [string[i:] for i in range(len(string))]

answer.sort() # answer를 오름차순으로 정렬

print("\n".join(answer))