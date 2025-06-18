# 경우가 뭐뭐 있지?
 
# 양가격 후가격 반가격 양개수 후개수
A, B, C, X, Y = map(int, input().split())

# 반반으로 전부 구매
total1 = C * max(X, Y) * 2

# 반반으로 사고 남은거 양이나 후로 채우기
if X > Y:
    total2 = C * Y * 2 + A * (X - Y)
else:
    total2 = C * X * 2 + B * (Y - X)

# 양, 후로 각각 구매
total3 = A * X + B * Y

# 3개뿐인가? 더 없나?
print(min(total1, total2, total3))