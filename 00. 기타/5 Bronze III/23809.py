def main():

    n = int(input())

    for _ in range(n):
        print("@" * n, end= "")
        print("   " * n, end= "")
        print("@" * n, end= "")
        print()
    for _ in range(n):
        print("@" * n, end= "")
        print("  " * n, end= "")
        print("@" * n, end= "")
        print()
    for _ in range(n):
        print("@@@" * n, end= "")
        print()
    for _ in range(n):
        print("@" * n, end= "")
        print("  " * n, end= "")
        print("@" * n, end= "")
        print()
    for _ in range(n):
        print("@" * n, end= "")
        print("   " * n, end= "")
        print("@" * n, end= "")
        print()

if __name__ == "__main__":
    main()