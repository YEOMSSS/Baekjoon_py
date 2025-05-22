'''
예제 입력 1 
1
Simon says smile.
예제 출력 1 
 smile.
예제 입력 2 
3
Simon says raise your right hand.
Lower your right hand.
Simon says raise your left hand.
예제 출력 2 
 raise your right hand. 
 raise your left hand. 
예제 입력 3 
3
Raise your right hand.
Lower your right hand.
Simon says raise your left hand.
예제 출력 3 
 raise your left hand. 
'''
import sys
input = sys.stdin.readline

cnt = int(input())

for _ in range(cnt):
    string = input().strip()
    if string[:10] == "Simon says":
        print(string[10:])
