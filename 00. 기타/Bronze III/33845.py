# 250515

remove_set = set(input()) # 없앨 문자들
string = list(input()) # 없앰 당할 문자들

result = [x for x in string if x not in remove_set] # 이런거 할 때 set이 빠르대요.
print(*result, sep= "")