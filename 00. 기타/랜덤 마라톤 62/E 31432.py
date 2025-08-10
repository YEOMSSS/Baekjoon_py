# 수를 중복해서 쓸 수 있다.
# 수는 아무거나 출력하면 된다.

# 그냥 세 번 쓰면 되지롱

N = int(input())

nums = list(map(int, input().split()))

if N == 0:
    print("NO")
else:
    print("YES")
    print(nums[0] * 111)