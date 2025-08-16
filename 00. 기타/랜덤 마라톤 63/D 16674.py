from collections import Counter

N = list(input())
N_count = Counter(N)
set_N = set(N)

if not ("3" in set_N or "4" in set_N or "5" in set_N or "6" in set_N or "7" in set_N or "9" in set_N):
    if set(N) == set(["2", "0", "1", "8"]):
        if N_count["2"] == N_count["0"] == N_count["1"] == N_count["8"]:
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)