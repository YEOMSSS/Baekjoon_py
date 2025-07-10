'''
표준 출력을 flush해야 하는 이유

콘솔 혹은 파일 입출력은 사칙연산이나 값을 대입하는 등의 기본적인 연산에 비해 상대적으로 느린 작업이다.
따라서 많은 프로그래밍 언어의 기본 출력 기능은 출력을 요청받은 값들을 한 공간에 쌓아두고,
적당한 때에 한꺼번에 출력되도록 한다. 이 공간을 버퍼(buffer)라고 부른다.

그러나 이 문제에서는 채점기가 프로그램의 출력을 실시간으로 확인해야 답변을 줄 수 있다.
따라서 버퍼를 직접 비우는 작업이 필요하고, 이 작업을 flush라고 한다.
'''

for a in range(1, 10):
    # A가 a인지 물어보고 flush를 한다.
    # print에 flush 파라미터를 넣으면 된다.
    print("? A", a, flush=True)

    # 채점기의 답변을 입력받는다.
    resp = int(input())

    if resp == 1:
        break

for b in range(1, 10):
    print("? B", b, flush=True)
    resp = int(input())

    if resp == 1:
        break
    
print("!", a + b)