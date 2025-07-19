while True:
    N = int(input())
    if N == 0:
        break
    result = 0
    for i in range(1, N + 1):
        result += i ** 2
    print(result)