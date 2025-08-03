string = input().rstrip()
key = input()

key_len = len(key)
idx = 0
for char in string:
    if char == " ":
        print(" ", end= "")
    else:
        print(chr((ord(char) - ord(key[idx]) - 1) % 26 + ord("a")), end= "")
    idx = (idx + 1) % key_len

