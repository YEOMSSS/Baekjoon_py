Data = [3, 2, 5, 4, 1]
max_val = Data[0]
where_max = 0

for now in range(1, len(Data)):
    # 다음 val이 현재 maxval보다 크면 교체
    if Data[now] > max_val:
        max_val = Data[now]
        where_max = now

print(max_val, where_max)
