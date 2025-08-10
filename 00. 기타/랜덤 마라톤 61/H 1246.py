# 영양란으로 둔갑하고 꼴에 죄책감 느끼는건 뭐야

import sys

N, M = map(int, input().split())
prices = sorted([int(input()) for _ in range(M)])

result_revenue = 0
result_price = 0

for i in range(M):
    price = prices[i]
    # 현재 가격 이상을 제시한 소비자 수 = M - i
    consumers = M - i
    eggs_sold = min(N, consumers)
    revenue = price * eggs_sold
    if revenue > result_revenue:
        result_revenue = revenue
        result_price = price

print(result_price, result_revenue)

# 대체 왜 맞았는지 모르겠다.