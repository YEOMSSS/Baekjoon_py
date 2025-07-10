'''
string = input()

answer = len(string) // len(set(string))

print(answer)
'''
'''
string = input()
print(string.count(string[0]))
'''
# 이게 한줄로 된다고?

print((string := input()).count(string[0]))