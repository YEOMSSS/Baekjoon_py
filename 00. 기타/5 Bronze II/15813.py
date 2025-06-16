'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = range(1, 27)

N = int(input())
name = input()

answer = 0
for char in name:
    answer += score[alphabet.index(char)]

print(answer)
'''
# 아스키코드로

N = int(input())
name = input()

answer = 0
for char in name:
    answer += ord(char) - 64

print(answer)
