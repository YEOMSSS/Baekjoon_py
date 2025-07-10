# x / N = i...i (i는 나머지니까, i < N)
# i * N + i = X (X는 자연수니까, i != 0)
# i * (N + 1) = X
# i에 1부터 넣어보자.


N = int(input())

result = 0
for i in range(1, N):
    result += i * (N + 1)

print(result)