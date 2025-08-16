N = int(input())
nums = list(map(int, input().split()))

# 1 2 3 4 5 6 7.. 순서대로 들어있긴 해야한다.
# 1이 없으면 바로 탈락이지, 뭐. 검사해볼까.

temp = 1
result = 0
for num in nums:
    if num == temp:
        temp += 1
    else:
        result += 1

print(result)