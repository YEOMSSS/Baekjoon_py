
def main():
    n = int(input())

    nums = list(map(int, input().split()))

    ans = sum(nums) + 8 * (n - 1)

    print(ans // 24, ans % 24)

if __name__ == "__main__":
    main()