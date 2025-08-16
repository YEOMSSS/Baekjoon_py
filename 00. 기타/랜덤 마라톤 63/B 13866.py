A, B, C, D = map(int, input().split())

# 12 34, 13 24, 14 23 말고 더 없는듯.
result = []
result.append(abs((A + B) - (C + D)))
result.append(abs((A + C) - (B + D)))
result.append(abs((A + D) - (C + B)))

print(min(result))