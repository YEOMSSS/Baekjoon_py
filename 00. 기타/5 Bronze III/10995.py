N = int(input())

for _ in range(N // 2):
    print("* " * N)
    print(" *" * N)
if N % 2 == 1:
    print("* " * N)