import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

# 올라가기 시작하는 동안은 스위치가 꺼져 있다.
# 내려가는 순간 True가 된다.
check = False

prev = 0
for num in nums:

    # 내려가는 동안 스위치가 계속 켜진다.
    if prev > num:
        check = True

    # 스위치가 켜져 있는 상태에서 올라가면 즉시 종료
    elif prev < num and check:
        print("NO")
        break
    
    # 직전 수와 동일하면 즉시 종료
    elif prev == num:
        print("NO")
        break

    # prev 갱신
    prev = num

# return 없이 진행되었다면 조건 만족
else:
    print("YES")

# 출력이 다 대문자였네...
