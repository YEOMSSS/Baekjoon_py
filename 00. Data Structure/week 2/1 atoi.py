Data = ["1", "2", "3"]

val = 0
for i in range(len(Data)):
    # int()를 사용하는 경우
    val = val * 10 + int(Data[i])
    # ascii를 사용하는 경우
    # val = val * 10 + ord(Data[i]) - 48

print(val)
