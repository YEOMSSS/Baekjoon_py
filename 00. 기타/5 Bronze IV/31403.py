#250517

import sys
'''
A, B, C = sys.stdin.read().split()

print(int(A) + int(B) - int(C))
print(int(A + B) - int(C))
'''
A, B, C = map(int, sys.stdin.read().split())

print(A + B - C)
print(int(str(A) + str(B)) - C)

# 걸리는 시간은 똑같네.