import sys
input = sys.stdin.readline

def main():

    while True:
        m, f = map(int, input().split())

        if m == 0 and f == 0:
            break

        print(m + f)

if __name__ == "__main__":
    main()