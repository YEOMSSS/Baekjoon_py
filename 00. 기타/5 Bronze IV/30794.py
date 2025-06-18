lv, judge = input().split()
lv = int(lv)

match judge:
    case "miss":
        print(0)
    case "bad":
        print(200 * lv)
    case "cool":
        print(400 * lv)
    case "great":
        print(600 * lv)
    case "perfect":
        print(1000 * lv)