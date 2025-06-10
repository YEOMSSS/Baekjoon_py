'''
import sys
input = sys.stdin.readline

def main():

    n = int(input())
    A_list = list(map(int, input().split()))

    m = int(input())
    nums = list(map(int, input().split()))

    for num in nums:
        if num in A_list:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()
'''
# 시간초과가 나버린다고?
# list에서의 in활용은 시간복잡도가 O(n)이니까.. 사실상 이중포문
# 그럼 set은 어떨까??

import sys
input = sys.stdin.readline

def main():

    n = int(input())
    A_list = set(map(int, input().split())) # set을 써보자.

    m = int(input())
    nums = list(map(int, input().split()))

    for num in nums:
        if num in A_list:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()

# 이분탐색은 나중에 하자고. 나중에...