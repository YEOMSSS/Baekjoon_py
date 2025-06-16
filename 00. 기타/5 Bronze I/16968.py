def main():
    types = input()

    prev = ""
    answer = 1
    for type in types:
        match type:
            case "c":
                if prev == "c":
                    answer *= 25
                else:
                    answer *= 26
            case "d":
                if prev == "d":
                    answer *= 9
                else:
                    answer *= 10
        prev = type

    print(answer)

if __name__ == "__main__":
    main()