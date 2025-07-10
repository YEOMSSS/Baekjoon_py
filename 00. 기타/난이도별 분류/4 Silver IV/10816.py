
import sys
input = sys.stdin.readline

from collections import Counter

def main():

    N = int(input())
    N_nums = list(map(int, input().split()))

    num_counter = Counter(N_nums)

    M = int(input())
    M_nums = list(map(int, input().split()))

    # counter에서 num의 value를 가져오고 없으면 0을 반환
    answer = [str(num_counter.get(num, 0)) for num in M_nums]
    print(" ".join(answer))

if __name__ == "__main__":
    main()