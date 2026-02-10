for ch in input():
    print(ch * sum(map(int, list(str(ord(ch))))))

print("\n".join(ch * sum(map(int, str(ord(ch)))) for ch in input()))
