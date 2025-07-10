def main():

    n = int(input())

    nums = list(range(1, n + 1))

    while len(nums) != 1:
        for i in range(len(nums) - 1, -1, -1):
            if i % 2 == 0:
                nums.pop(i)

    print(*nums)

if __name__ == "__main__":
    main()