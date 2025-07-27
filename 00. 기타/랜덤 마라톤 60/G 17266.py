import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

locates = list(map(int, input().split()))

# 맨앞가로등, 맨뒤가로등 최소길이 넣고 시작
distances = [locates[0], N - locates[-1]]

# 가로등 사이 거리 //2 저장
# 올림나눗셈으로 가로등사이거리가 홀수일때 +1처리 (x+y-1)//2
for i in range(M - 1):
    length = (abs(locates[i] - locates[i + 1]) + 2 - 1) // 2
    distances.append(length)

print(max(distances))