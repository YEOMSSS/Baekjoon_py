def get_primes_under_8000():
    # 8000 이하의 소수 리스트 생성
    sieve = [True] * 8001
    for i in range(2, int(8000**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 8001, i):
                sieve[j] = False
    return [i for i in range(2, 8001) if sieve[i]]


def solve():
    primes = get_primes_under_8000()

    # 5000자리 근처에서 시작 (예: 10^4999 + 난수)
    # 실제로는 고정된 숫자로 시작해서 2씩 더하며 찾아도 충분함
    p = 10**4999 + 1

    while True:
        # p와 p+2가 8000 이하 소수들로 나누어떨어지는지 검사
        p_ok = True
        for pr in primes:
            if p % pr == 0:
                p_ok = False
                break

        if p_ok:
            # p가 통과했다면 p+2도 검사
            p2_ok = True
            for pr in primes:
                if (p + 2) % pr == 0:
                    p2_ok = False
                    break

            if p2_ok:
                print(p)
                print(p + 2)
                break

        p += 2  # 다음 홀수로
