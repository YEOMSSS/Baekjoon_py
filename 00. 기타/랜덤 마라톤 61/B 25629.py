# 홀수 개수 = 짝수 개수 or 홀수개수가 하나 더 많으면 성립

N = int(input())

nums = list(map(int, input().split()))

odds = 0
evens = 0
for num in nums:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

if odds == evens or odds == evens + 1:
    print(1)
else:
    print(0)