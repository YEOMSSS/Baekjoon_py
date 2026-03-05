Data = [i for i in range(1, 7)]
# Data = list(range(1, 7))
howmany = len(Data)

# 노가다의 경우
# 이 노가다의 과정은 왜 필요한가? 일단 해봐야 아는거지.
# Data[0], Data[howmany - 1] = Data[howmany - 1], Data[0]
# Data[1], Data[howmany - 1 - 1] = Data[howmany - 1 - 1], Data[1]
# Data[2], Data[howmany - 1 - 1 - 1] = Data[howmany - 1 - 1 - 1], Data[2]

# 이런 효율적인 코드는 바로바로 나오는 게 아니다. 노가다를 꼭 해보자. 노트에 직접 써보고.
for i in range(howmany // 2):
    Data[i], Data[howmany - i - 1] = Data[howmany - i - 1], Data[i]

print(*Data)

# 기본적으로 reverse가 존재하긴 한다.
# 존재하지만, 고급 간장을 만들기 위해 시간을 들여보자.
Data = list(range(1, 7))
Data.reverse()
print(*Data)
