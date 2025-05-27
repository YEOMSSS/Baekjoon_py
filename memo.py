num = int(input())

pack_prices = list(map(int, input().split()))

answer = 0
while num != 0:
    card_prices = []

    index_max = 0
    for i in range(num):
        if pack_prices[i] * (index_max + 1) > pack_prices[index_max] * (i + 1):
                    index_max = i

    answer += pack_prices[index_max] * (num // (index_max + 1))
    # 가장 비싼 팩을 최대한 많이 구매한다.
    
    num %= index_max + 1

print(answer)