import sys
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())
pieces = [[] for _ in range(N + 1)]
for _ in range(N):
    A, V, H = map(int, input().split())
    pieces[A].append((V, H))

max_idx = -1
max_area = 0
for i in range(1, N + 1):  # 1부터 N까지
    piece = pieces[i]
    if len(piece) < 1:
        continue
    max_V, max_H = 0, 0
    min_V, min_H = R, C
    for V, H in piece:
        max_V = max(max_V, V)
        min_V = min(min_V, V)
        max_H = max(max_H, H)
        min_H = min(min_H, H)
    area = (max_V - min_V + 1) * (max_H - min_H + 1)
    if area > max_area:
        max_idx = i
        max_area = area

print(max_idx, max_area)



'''
1 1
1
1 1 1
0 0
'''
# 84%... 왜 틀리는 거지??
# 위 반례로 틀린 코드.
'''
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())
pieces = [[] for _ in range(N + 1)]
for _ in range(N):
    A, V, H = map(int, input().split())
    pieces[A].append((V, H))

max_idx = 0
result = 0
for i, piece in enumerate(pieces):
    if len(piece) == 0 or len(piece) == 1:
        continue
    else:
        max_V, max_H = 0, 0
        min_V, min_H = R, C
        for V, H in piece:
            max_V = max(max_V, V)
            min_V = min(min_V, V)
            max_H = max(max_H, H)
            min_H = min(min_H, H)
        area = (max_V - min_V + 1) * (max_H - min_H + 1)
        if area > result:
            max_idx = i
            result = area
            
print(max_idx, result)
'''