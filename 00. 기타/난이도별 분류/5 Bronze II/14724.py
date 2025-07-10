
N = int(input())

clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

prev = -1
answer = ""
for i in range(9):
    max_score = max(list(map(int, input().split())))
    if max_score > prev:
        prev = max_score
        answer = clubs[i]

print(answer)