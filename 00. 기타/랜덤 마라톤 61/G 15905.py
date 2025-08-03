N = int(input())

participants = [list(map(int, input().split())) for _ in range(N)]

participants.sort(key= lambda x: (-x[0], x[1]))

fifth = participants[4][0]

result = 0
for participant in participants[5:]:
    if participant[0] == fifth:
        result += 1
    else:
        break

print(result)
