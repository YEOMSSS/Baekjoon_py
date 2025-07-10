T = int(input())

score_board = [0] * 5

subject_score = list(map(int, input().split()))

for i in range(len(subject_score)):
    score_board[i] = subject_score[i]

# 0국어 1수학 2영어 3탐구 4제2외국어

if score_board[0] > score_board[2]:
    result1 = (score_board[0] - score_board[2]) * 508
else:
    result1 = (score_board[2] - score_board[0]) * 108

if score_board[1] > score_board[3]:
    result2 = (score_board[1] - score_board[3]) * 212
else:
    result2 = (score_board[3] - score_board[1]) * 305

result3 = score_board[4] * 707

answer = (result1 + result2 + result3) * 4763

print(answer)

# 귀찮고 까다로운 문제
# 그냥 더러움