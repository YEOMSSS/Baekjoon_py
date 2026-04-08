Queue = []
howmany = 41

for who in range(1, howmany + 1):
    Queue.append(who)

while len(Queue) != 2:
    alive1 = Queue.pop(0)
    alive2 = Queue.pop(0)
    dead = Queue.pop(0)

    print(alive1, alive2, dead)
    Queue.append(alive1)
    Queue.append(alive2)

print(Queue.pop(0))  # 이게 요세푸스
print(Queue.pop(0))  # 이게 원래 살아야 했을 사람.
