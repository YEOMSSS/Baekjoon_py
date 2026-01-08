import sys

input = sys.stdin.readline

# 큰수끼리 먼저 묶어주는게 이득인 것 같음.
# 그런데 묶지 않아야 할 경우가 있는 것 같다. 곱해서 더 작아지는 경우.
# 1 1은 더하는게 곱할때보다 크다. 1의 경우도 곱하지 말고 더해야겠네. 2부터는 곱하는게 무조건 더 크다.
# 1은 무조건 더하는게 맞다. 곱하면 1손해고, 0이랑 곱해도 1손해고. 음수랑 곱하면 무조건 손해니까.
# 음수끼리는 작은거부터 곱해서 남는건 스킵해야하고.
# 만약 0이 있으면 음수 하나 남은거랑 곱하거나, 양수 하나 남으면 그냥 버리고.

# 1과 0, 음수만 신경써주면 되나?


def main() -> None:

    N = int(input())

    positives = []
    negatives = []
    check_zero = False
    count_one = 0

    for _ in range(N):
        num = int(input())
        if not num:
            check_zero = True
        elif num == 1:
            count_one += 1
        elif num > 0:
            positives.append(num)
        else:  # num < 0
            negatives.append(num)

    positives.sort(reverse=True)
    negatives.sort()

    # 1은 무조건 더하는게 이득이다. 어느 것에 곱해도 손해임.
    result = count_one

    # 1을 제외한 양수에 대하여 큰 수부터 둘씩 묶어 곱해 더한다.
    for i in range(0, len(positives) // 2):
        result += positives[i * 2] * positives[i * 2 + 1]
    # 둘씩 묶고 남은 양수는 무조건 더한다.
    if len(positives) % 2:
        result += positives[-1]

    # 음수는 작은 것부터 묶어 곱해 더한다.
    for i in range(0, len(negatives) // 2):
        result += negatives[i * 2] * negatives[i * 2 + 1]
    # 음수가 하나 남고, 0이 입력에 있었다면 남은 음수는 0에 곱해 없애준다.
    if len(negatives) % 2:
        if not check_zero:
            result += negatives[-1]

    print(result)


if __name__ == "__main__":
    main()
