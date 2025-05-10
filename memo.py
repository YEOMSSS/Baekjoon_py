size = int(input())
cnt = 0
for i in range(1, size - 1):    
    cnt += (size - i) * (size - i - 1) / 2
print(int(cnt))
print(3)