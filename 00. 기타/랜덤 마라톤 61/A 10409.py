N, T = map(int, input().split())

times = list(map(int, input().split()))

total_time = 0
for idx, time in enumerate(times):
    total_time += time
    if total_time > T:
        print(idx)
        break
# 모든 일을 처리할 수 있는 경우
else:
    print(N)

