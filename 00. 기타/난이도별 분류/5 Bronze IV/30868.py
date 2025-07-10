def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        if n < 5:
            print("|" * (n % 5))
            continue

        print("++++ " * (n // 5), end = "")
        print("|" * (n % 5))

if __name__ == "__main__":
    main()