# 빨간색: 620nm 이상 780nm 이하
# 주황색: 590nm 이상 620nm 미만
# 노란색: 570nm 이상 590nm 미만
# 초록색: 495nm 이상 570nm 미만
# 파란색: 450nm 이상 495nm 미만
# 남색: 425nm 이상 450nm 미만
# 보라색: 380nm 이상 425nm 미만

lam = int(input())

if lam >= 620:
    print("Red")
elif lam >=590:
    print("Orange")
elif lam >= 570:
    print("Yellow")
elif lam >= 495:
    print("Green")
elif lam >= 450:
    print("Blue")
elif lam >= 425:
    print("Indigo")
else:
    print("Violet")