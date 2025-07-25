import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())

    nums = list(map(int, input().split()))

    result = []
    while nums:
        current = nums.pop()
        discounted = current // 4 * 3
        if discounted in nums:
            nums.remove(discounted)
            result.append(discounted)

    print(f"Case #{i + 1}: {' '.join(map(str, result[::-1]))}")
