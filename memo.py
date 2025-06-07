
def main():
    n = int(input())

    a, b = 2, 1

    # 0일때 ㅗㅜ 1일때 =
    for _ in range(n - 1): # 이미 2,1일때 한번 실행됐으니 -1
        a, b = (a * 3 + b * 2), (a + b)
    
    print((a + b))

if __name__ == "__main__":
    main()