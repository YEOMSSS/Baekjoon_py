N = int(input())

temp = 0
while True:
    temp += 1

    if N <= temp:
        print(temp + 1 - N, N)
        break
    else:
        N -= temp

