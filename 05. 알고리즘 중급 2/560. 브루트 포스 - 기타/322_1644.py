# Authored by : marigold2003
# Date : 2026-02-28
# Link : https://www.acmicpc.net/problem/1644


import sys

input = sys.stdin.readline


# [Summary] 소수의 연속합

# 자연수 N(4M)을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 일단 N(4M)까지 소수를 구해놓아야 한다. 이건 체를 쓰고.
    # 그리고 소수 배열에서 투포인터를 쓰자. 가변길이슬라이딩윈도우로

    ##########

    N = int(input())

    # 체로 소수 거르기
    def sieve(n):
        is_prime = [True] * (n + 1)

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False

        # 소수인 것들만 모은 리스트 반환
        return [i for i in range(2, n + 1) if is_prime[i]]

    primes = sieve(N)
    len_primes = len(primes)

    end, count, curr_sum = 0, 0, 0
    for start in range(len_primes):

        # 현재합이 목표보다 적으면 end 연장
        while curr_sum < N and end < len_primes:
            curr_sum += primes[end]
            end += 1

        # 현재합이 조건만족시 카운트 +1
        if curr_sum == N:
            count += 1

        curr_sum -= primes[start]

    print(count)

    ##########

    return


# [Review]

# 가볍게 짜 봤다.
# 에테체 + 투포인터


if __name__ == "__main__":
    main()
