# 지니어스에서 본 것 같은 게임이네.

N = int(input())

cards = list(map(int, input().split()))

score = 0
prev = 0
for card in cards:
    if prev + 1 == card:
        pass
    else:
        score += card
    prev = card

print(score)