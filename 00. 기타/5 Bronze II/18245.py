'''
하영이는 이 길고 많은 줄로 이루어진 문장을 어떻게 해석해야 할지 고민하던 중, 풀숲 속에 놓인 석판을 발견하였다.

[ i번째 줄의 문장은 문장의 첫 번째 글자에서 시작하여 i칸씩 건너뛰며 읽어야 한다 ]

하지만, 하영이는 이 암호를 직접 해석하기에는 시간이 부족하다는 것을 깨달았다.
하영이를 살려주기 위해서 이 암호가 무슨 뜻인지 해석해주는 프로그램을 만들어주자!

입력
첫째 줄부터 최대 100개의 줄에 알파벳 대문자로 이루어진 해석해야 할 문장이 주어진다. 문장의 길이는 104이하인 자연수이다.

해석해야 할 문장이 모두 주어진 후, 마지막 문장은 Was it a cat I saw? 로 주어지고, 마지막 문장은 해석하지 않는다.

출력
한 줄에 한 문장씩 해당 줄의 문장에서 해석한 암호를 출력한다.

예제 입력 1 
HZAOPAPCYSUENCBOINRDTCHODNATY
Was it a cat I saw?
예제 출력 1 
HAPPYUNBIRTHDAY
예제 입력 2 
RAEBDCVDEELFVGEHT
SIJEKLUMNLOPGQRI
ISTURVWXEYZANBCDE
WEFGHEIJKLNMNOPDQRSTY
YUVWXYEZABCDREFGHII
JJKLMNOOPQRSTUY
Was it a cat I saw?
예제 출력 2 
REDVELVET
SEULGI
IRENE
WENDY
YERI
JOY
'''

import sys
input = sys.stdin.readline

i = 1
while True:
    i += 1
    string = input().strip()
    if string == "Was it a cat I saw?":
        break
    print(string[::i])
