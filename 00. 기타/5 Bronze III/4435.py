import sys
input = sys.stdin.readline

T = int(input())

Good_scores = [1, 2, 3, 3, 4, 10]
Evil_scores = [1, 2, 2, 2, 3, 5, 10]
for t in range(1, T + 1):
    Good = list(map(int, input().split()))
    Evil = list(map(int, input().split()))

    Good_score_sum = 0
    for i, num in enumerate(Good):
        Good_score_sum += num * Good_scores[i]
    Evil_score_sum = 0
    for i, num in enumerate(Evil):
        Evil_score_sum += num * Evil_scores[i]

    if Good_score_sum == Evil_score_sum:
        print(f"Battle {t}: No victor on this battle field")
    elif Good_score_sum > Evil_score_sum:
        print(f"Battle {t}: Good triumphs over Evil")
    else:
        print(f"Battle {t}: Evil eradicates all trace of Good")