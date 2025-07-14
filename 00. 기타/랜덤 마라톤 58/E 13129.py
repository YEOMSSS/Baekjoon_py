A, B, N = map(int, input().split())

for i in range(1, N + 1):
    height = A * N + B * i
    print(height, end= " ")

