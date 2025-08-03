import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

conditions = [True] * (N + 1)
count_True = N
for _ in range(Q):
    command = input().split()
    query = command[0]
    if query == "1" or query == "2":
        idx = int(command[1])   
        if query == "1" and conditions[idx] == True:
            conditions[idx] = False
            count_True -= 1
        elif query == "2" and conditions[idx] == False:
            conditions[idx] = True
            count_True += 1
    elif query == "3":
        print(count_True)
