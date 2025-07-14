import sys
input = sys.stdin.readline

N = int(input())

weight = 0
price = 0
for _ in range(N):
    box, W, H, L = input().split()
    W, H, L = map(int, (W, H, L))

    if box == "A":
        apple_count = (W // 12) * (H // 12) * (L // 12)
        apple_weight = apple_count * 500 + 1000
        apple_price = apple_count * 4000

        weight += apple_weight
        price += apple_price

    if box == "B":
        weight += 6000

print(weight)
print(price)