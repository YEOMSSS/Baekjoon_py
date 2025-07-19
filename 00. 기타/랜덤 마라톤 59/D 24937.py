'''
SciComLove
'''

word = "SciComLove"
N = int(input()) % len(word)

result = word[N:] + word[:N]
print(result)