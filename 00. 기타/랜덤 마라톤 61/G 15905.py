import sys
input = sys.stdin.readline

N = int(input())

participants = [list(map(int, input().split())) for _ in range(N)]

# participants[0]에 대해 내림차순 우선, 동일 시 [1]에 대해 오름차순 정렬
participants.sort(key= lambda x: (-x[0], x[1]))

fifth = participants[4][0]

result = 0
for participant in participants[5:]:
    if participant[0] == fifth:
        result += 1
    else:
        break

print(result)
