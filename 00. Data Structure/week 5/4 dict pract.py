Data = "Hello World"

result = {"대문자": 0, "소문자": 0}  # Counter가 쓰고싶어지는 순간.

for ch in Data:
    # if ch.isupper(): # 대문자판정
    if "A" <= ch <= "Z":  # 아스키로
        result["대문자"] += 1
    # if ch.islower():
    elif "a" <= ch <= "z":
        result["소문자"] += 1

print(result)
print(result["대문자"])
print(result["소문자"])
