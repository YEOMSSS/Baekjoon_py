백준 단계별로 (12단계까지) : 컷   
알고리즘 강의(기초부터 중급까지)문제 풀기   
기초1 : 진행중, 기초2, 중급1   

시간제한이 걸리면 PyPy3으로 제출.   
같은 코드를 PyPy3으로 제출하면 메모리를 python3보다 두배로 먹긴 해도, 두배 빨라진다.   
# BAEKJOON
2025.05.13 100 solve 달성!!   
2025.05.17 CLASS 1++
2025.05.20 CLASS 2
2025.06.03 GOLD V 달성!!
2025.06.04 200 solve 달성!!

## 다시 풀어보고 싶은 문제
02.201.110_17298 오큰수 : 오로지 내 힘으로 푼 문제가 아니다.   
00.Bronze V.10699 : 현재 시각을 어떻게 나타내는지 알아두자.   
02.203.113_1918 후위 표기식 : 다시 풀어보면 또 헷갈릴 듯.    
02.301.129_2089 -2진수 : 이건 진짜 또 풀어볼만 하다. 진수변환의 끝.
00.Bronze I.2246 : 머리가 굉장히 아픈 문제.
02.402.158_17404 RGB거리 2 : 헛군데를 잘못 파면 어떻게 되는지 알려주는 문제.


# 00. 기타
solved.ac에서 마라톤이나 CLASS를 푼 찌꺼기들

#### dict.get(key, default)
dict[key]는 key가 존재하지 않으면 keyError가 나지만,   
dict.get(key, default)는 default를 반환한다. default가 없다면 None을 반환한다.   

#### collections.Counter(iterable)
iterable의 개수를 각각 세서 dict의 형태로 반환한다.    
사실 Counter의 형태로 반환하는 거지만, dict와 같은 역할을 수행할 수 있다.   

#### '구분자'.join(문자열로 이루어진 iterable)
`print("\n".join(map(str, iterable)))` iterable의 요소를 한줄씩 출력한다.   
.join은 str일 때만 작동함에 유의   

    print(', '.join(['apple', 'banana', 'kiwi']))         # 리스트
    print(' | '.join(('a', 'b', 'c')))                    # 튜플
    print('-'.join('abc'))                                # 문자열 자체
    print('\n'.join(str(x) for x in range(5)))            # 제너레이터

#### list.sort()
`words.sort(key=len)`  # 길이 기준 정렬   
`words.sort(key=str.lower)`  # 대소문자 무시 알파벳 정렬   
`words.sort(key=lambda x: (len(x), x))`  # 길이 우선, 알파벳 보조 정렬   

`words.sort(reverse=True)`  # 기본 비교 기준의 역순   
`words.sort(key=len, reverse=True)`  # 길이 기준 내림차순   

`words.sort(key=lambda x: (len(x), x.lower()), reverse=False)` # 길이정렬 후 같으면 알파벳정렬

    words = ["apple", "fig", "pear", "banana", "kiwi"]
    words.sort(key=lambda x: (len(x), x))
    print(words)
    # 출력: ['fig', 'kiwi', 'pear', 'apple', 'banana']

#### sorted(iterable)
sorted()는 list.sort()와 동일한 사용방식을 가지나, iterable에 사용할 수 있다.   
원본을 정렬하는 sort()와 달리 값을 반환한다. 값은 list형태로 반환된다.

    words = ["apple", "fig", "pear", "banana", "kiwi"]
    sorted_words = sorted(words, key=lambda x: (len(x), x))
    print(sorted_words)
    # 출력: ['fig', 'kiwi', 'pear', 'apple', 'banana']

#### 올림 계산 (math.ceil(a / b)의 정수형 풀이)
어떤 수 a를 b로 나눌 때, 나머지가 생기면 몫에 +1을 해야 하는 경우
(a + b - 1) // b 를 하면 올림한 몫을 구할 수 있다.

#### divmod(a, b)
divmod(a, b) 는 (a // b, a % b) 튜플을 반환한다.


# 03. 알고리즘 기초 2/2

## 510. 브루트 포스 (N과 M) 250611 ~ 
주로 백트래킹에 대해 다루는 부분이다.

#### range(start, end)
start부터 end-1까지의 수를 반환하는 iterable이다. 리스트가 아니다.   
range 타입으로, 숫자들을 미리 저장하는 것이 아니라 필요할 때 값을 생성하는 방식으로 동작한다.   

#### itertools.permutations(iterable, num)
list에서 서로 다른 요소 중 num개를 선택하는 **순열**을 중복 없이 **튜플** 형태로 생성한다.  

#### itertools.combinations(iterable, num)
list에서 서로 다른 요소 중 num개를 선택하는 **조합**을 중복 없이 **튜플** 형태로 생성한다.  
`pairs = list(combinations(arr, 2))` 형태로 사용한다.   
`pairs = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i + 1, len(arr))]` 은   
`pairs = [(i, j) for i, j in combinations(arr, 2)]` 로 나타낼 수 있다.

## 501. 브루트 포스 250608 ~ 250611

# 02. 알고리즘 기초 1/2 250513 ~ 250607

## 402. 다이나믹 프로그래밍 1 (도전) 250607 ~ 250607

## 401. 다이나믹 프로그래밍 1 (연습) 250602 ~ 250607
이게 참, 뭔가 한건 많은데 새로 나온게 없다고 해야하나.   
북마크해둔 문제들을 다시 풀어보는 것도 좋겠다.   

## 400. 다이나믹 프로그래밍 1 250524 ~ 250601
큰 문제를 작은 문제로 나누고, 그 결과를 재활용하여 전체 문제를 푸는 방식.   
알고리즘을 보고 "어차피 전 범위 다 보겠네?" -> 타뷸레이션   
"계산할 게 몇 개 안 되는데 가지가 많이 퍼지네?" -> 메모이제이션   

사용하는 함수가가 어렵다기보단 로직이 생각해내기가 어렵다.   
알고리즘이라는 게 다 그렇지 뭐..   
그래도 풀다 보니 좀 알겠다. 박다 보니 답이 나오는 것이다.

#### 최장 증가 부분 수열
LIS: Longest Increasing Subsequence

#### 메모이제이션 (top - down)
재귀하며 중복계산은 딕셔너리에 저장하고, 한번 한 계산은 재사용한다.

    import sys
    sys.setrecursionlimit(10**6)
    재귀 깊이를 늘리는 코드. 파이썬은 1000번이 제한이기 때문에 반필수다.
    다만 이걸 사용하면 보통 메모리가 초과된다.

#### 타뷸레이션 (bottom - up)
작은 문제부터 dp배열에 차곡차곡 계산해 넣는다.

## 303. 수학 1 (참고) 250524 ~ 250524

#### enumerate(iterable)
`for index, value in enumerate(iterable)` index와 value에 iterable의 인덱스와 값이 들어간다.   

## 301. 수학 1 (연습) 250522 ~ 250524

#### abs(num)
절댓값을 반환한다.

#### functools.reduce(function, iterable)
iterable의 처음 두 요소부터 시작해서 하나씩 function을 누적해 적용한다.
만약 iterable의 길이가 1이라면 함수를 호출하지 않고 하나뿐인 요소를 그대로 반환한다.

#### 진수 변환
10진수 -> 2진수 bin(255)[2:]  # '11111111'   
10진수 -> 8진수 oct(255)[2:]  # '377'   
10진수 -> 16진수 hex(255)[2:]  # 'ff'   

#### extend([a, b])
리스트를 풀어서 요소별로 추가 (평탄화)
append(a); append(b) 와 동일한 효과지만 한 번에 처리할 수 있다.

## 300. 수학 1 250520 ~ 250521

#### 최대공약수와 최소공배수 찾기
최대공약수(a, b) * 최소공배수(a, b) = a * b 이다.   
math.gcd(a, b) 는 최대공약수를 찾는다.   
math.lcm(a, b) 는 최소공배수를 찾는다.   
* 유클리드 호제법   
a와 b의 대소에 상관없이 a, b = b, a % b 를 반복해서 b가 0일 때 a가 최대공약수이다.

#### 에라토스테네스의 체
소수의 목록을 구해야 할 때 자주 사용한다. ~N 까지 소수의 목록을 구할 때

    sieve = [True] * (N + 1) # 0이 포함이므로 +1
    sieve[0] = sieve[1] = False # 0, 1은 소수가 아니다.

    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
이런 식으로 코드를 짜면 sieve에서 True는 소수인 인덱스에만 남게 된다.   
i 씩 건너뛰면서 리스트를 False로 바꾼다는 것은, i 의 배수를 지운다는 것이다.   
i * i 미만인 i 의 배수들은 이전 반복에서 이미 지워져 있다.   
시간복잡도는 O(N log log N). 굉장히 빠른 편이다. 대충 O(3N) 정도?

#### list.insert(index, val)
insert(2, 3) → 인덱스 2에 3을 넣고, 기존 요소는 오른쪽으로 밀린다.   


## 203. 자료구조 1 (참고) 250518 ~ 250519

#### print(f"{value:.2f}")
value를 소수점 둘째 자리에서 반올림해서 f-string 방식으로 출력

#### 알파벳의 판정법
* char.isupper() : 대문자인지 판정   
* char.islower() : 소문자인지 판정   
* char.isalpha() : 알파벳인지 판정

#### list.sort()
반환값이 없다. 그냥 따로 써주면 list를 유니코드 기준 오름차순으로 정렬한다.   

## 201. 자료구조 1 (연습) 250515 ~ 250517

#### 상태 플래그 (108번 참고)
상태 플래그는 프로그램이 현재 어떤 상태(모드)에 있는지를 표시하는 변수다.   
이 값을 바꾸면서 흐름이나 동작 방식을 다르게 제어할 수 있다.   

#### continue
그 자리에서 현재 반복을 멈추고, 다음 반복을 진행한다.   

#### collections.Counter
Counter(list) 의 형태로 list 안의 요소가 등장한 횟수를 {요소 : 횟수} 의 형태로 저장한다.   
딕셔너리처럼 작동함.   

## 200. 자료구조 1 250513 ~ 250515
stack : LIFO(Last In, First Out) 구조. 마지막에 넣은 걸 제일 먼저 꺼낸다. python에선 list로 사용.   
list.pop() : 괄호 안에 아무것도 없다면 리스트의 마지막 요소 list[-1]을 지운다.   
스택에서 가장 위(top) : stack[-1] 을 의미한다.   

    조건문을 한 줄로 써보자.
    print("YES" if balance == 0 else "NO") : 0이면 YES 출력, 0이 아니면 NO 출력
    balance += 1 if char == "(" else -1 : "("면 += 1, 아니면 += -1
print(*list, sep= "") : 리스트의 요소를 ""으로 나눠 출력한다.   
* deque : 양쪽 끝에서 삽입, 삭제가 가능한 큐. appendleft()와 popleft()를 사용할 수 있다.   

deque는 rotate가 가능한 자료구조이다.

    rotate(-1)은 왼쪽으로 한 칸, rotate(1)은 오른쪽으로 한 칸.
    Queue = deque([1, 2, 3, 4 ,5])
    Queue.rotate(-1) : deque([2, 3, 4, 5, 1])
    Queue.rotate(1) : deque([5, 1, 2, 3, 4]) 이런 느낌이다.
if list : list에 요소가 있으면 True, 요소가 없으면 False   
match - case 문법 : 패턴 매칭에서 if - elif 문법의 대체제. 리스트 같은 패턴도 match가 가능하다.   
즉, match는 값에 따라 어떤 일을 할지 결정할 때,   
if는 조건에 따라 흐름을 제어할 때 사용하는 것이 핵심 포인트이이다.   

    cmd = ["push", "10"]
    match cmd:
        case ["push", value]:
            print(f"{value}를 push")



# 01. 단계별로 풀어보기 1 ~ 12 250416 ~ 250513
## 12. 브루트 포스 250511 ~ 250513
tuple : 변경할 수 없는 리스트. 소괄호로 감싸서 만든다.   
list = map(int, input().split()) : map() 은 이터레이터다. list를 한번 사용하면 증발한다.   
list = list(map(int, input().split())) : 이건 계속 사용할 수 있다.   
a, b = map(int, input().split()) : 얘는 이터레이터의 값이 a, b에 복제된 거라 계속 사용할 수 있다.   
numer(numerator) : 보통 분자의 변수명으로 사용.   
denom(denominator) : 보통 분모의 변수명으로 사용.   
sum(x > 10 for x in [5, 11, 20]) : in의 쓰임을 잘 보자. 결과는 2다. sum 안에 있는 True를 1로 계산된다.

## 11. 시간 복잡도 250510 ~ 250511
시간 복잡도의 개념이 11번번 폴더에 있는 time_complexity.md 파일에 잘 설명되어 있다. 밑으로 발췌   
* n이 10배, 100배로 늘어날때, 실행시간도 10배, 100배로 늘어나면 O(n)이라고 합니다.   
* 같은 경우에 실행시간이 100배, 10000배로 늘어나면 O(n^2)이라고 합니다.   
* 같은 경우에 실행시간이 +1, +2만큼 늘어나면 O(log(n))이라고 합니다.   
* 같은 경우에 실행시간이 바뀌지 않으면 O(1)이라고 합니다.   

O형 시간복잡도 표현은 최고차항만 표시된다. 어차피 밑으로는 떨거지니까.   
코딩이 아니라 수학을 하는 느낌이다, 뭔가 w같아.   

## 10. 기하: 직사각형과 삼각형 250508 ~ 250510
float("inf"), float("-inf"): infinity는 어떤 수보다도 크기 때문에 초기값으로 자주 이용한다.   
arr[::2] : 슬라이싱이다. 배열을 처음부터 두 칸씩 뛰며 읽는다. 인덱스 0, 2, 4...   
arr[1::2] : 배열을 1번 인덱스부터 두 칸씩 뛰며 읽는다. 인덱스 1, 3, 5...   
* list[start:stop:step]   
* start: 시작 인덱스 (기본값은 처음부터)   
* stop: 멈출 인덱스 (기본값은 끝까지)   
* step: 건너뛰는 간격. 음수면 뒤에서 앞으로 (예시로, [::-1]은 리스트를 뒤집는다.)   

sys.stdin.read() (또는 open(0).read()): 한 번에 모든 입력을 받을 때 적합. EOF까지 문자열로 읽어옴.   
list = [int(input()) for _ in range(cnt)] : 이러면 엔터로 구분되게 cnt번 입력받을 수 있다.   

## 9. 약수, 배수와 소수 250507 ~ 250508
empty list는 False를, not empty list는 True를 return한다. if not list: 같은 게 가능함.   
솟수 판독기를 만들 땐 int(math.sqrt())를 사용해 제곱근까지만 판단하자. num ** 0.5 도 좋다.   
* for - else 문법 : for 안에서 break 없이 모든 반복이 끝나면 else를 실행.   
77번, 78번에서 소수 판정과 소인수분해 잘 알아두자.   

## 8. 일반 수학 1 250505 ~ 250507
iterable : 보통 반복 가능한 객체를 의미한다. 리스트, 문자열, 튜플 등   
int(string, base) : string을 base진법으로 변환한다. 그냥 int(x)에는 ,10 이 생략되어 있는 것이다. 기본 10진수.   
* math.ceil()은 올림, math.floor()는 내림.   
* int()는 소수점 아래를 그냥 지움.   
* round()는 반올림.  

올림(x / y) == 내림(x − 1 / y) + 1   

## 7. 2차원 배열 250504 ~ 250504
def matrix_maker(row): return [list(map(int, input().split())) for _ in range(row)]   
result = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)] : 보기 좋은 코드   
[a, b, c] + [d, e] == [a, b, c, d, e] : 리스트끼리 더하면 합쳐진 리스트가 된다.   
a, b = divmod(c, d) : c // d == a, c % d == b   
"abcde"를 list(input())으로 받으면 ['a', 'b', 'c', 'd', 'e']가 된다.   
"abcde"를 list(input().split()) 으로 받으면 ["abcde"]로 저장된다. 공백 기준 구분이므로.   

## 6. 심화 1 250502 ~ 250503
zip : 튜플로 묶어 쌍으로 돌아가게 한다. 나중에 해볼 것.   
for i in list1 + list2 : i에 합쳐진 리스트의 요소가 순서대로 들어간다.   
max(), min() : 최댓값과 최솟값을 찾는다.   
string.replace(x, y) : 문자열에서 x를 y로 바꾼 새로운 문자열을 반환한다. (리스트에는 replace()가 없음)   
list.count() : 리스트에 요소가 나온 횟수를 반환한다.   
string.upper() : string을 전부 대문자로 바꾼다.   
백슬래시 \ 뒤에 엔터를 치면, 한 줄로 이어진 코드로 처리된다. (줄바꿈 아님, 논리적 줄 연결임)   
코드가 이어지지 않는 단순한 줄바꿈은 ;로 할 수 있다.   
list.append() : 리스트에 요소를 추가한다.   
float() : 실수로 자료형을 변환한다.   
break : 그 자리에서 반복문 전체를 종료시킨다.   

## 5. 문자열 250430 ~ 250502
문자열에는 리스트에서 사용하는 함수를 대부분 사용할 수 있다.   
string[] + string[] : 공백 없이 합쳐져 붙는다.   
ord(), chr() : 문자를 아스키코드로, 아스키코드를 문자로 바꾸는 함수. 이 둘을 이용하면 알파벳 리스트를 쉽게 만들 수 있다.   
print(sum([int(f) for f in input()])) : 그냥 보기 좋아서 넣었다.   
string.find(x)는 문자열 안에 x가 있으면 첫 인덱스를 반환하고, 없으면 -1을 반환한다. 단, string.index(x)는 없을 경우 오류 발생.   
.strip()은 문자열의 앞뒤 공백을 제거한다. 사용 예시: input().strip().split()   
for char in string : 이런 식으로 리스트처럼 반복문을 사용할 수 있다. 한 글자씩 들어간다.   
* input(EOF) -> EOFError 발생   
* sys.stdin.readline(EOF) -> "" 빈 문자열 반환(32번 참고)   
* sys.stdin.read(EOF) -> EOF 만난 시점까지 읽은 전체 입력 문자열로 반환   

## 4. 1차원 배열 250428 ~ 250430
list.index() : 요소가 몇 번째 인덱스에 있는지 찾아준다.   
[0] * 5 == [0, 0, 0, 0, 0] 리스트를 쉽게쉽게 만들자.   
list(range(1, 6)) == [1, 2, 3, 4, 5] 리스트를 케이크처럼 쉽게 먹는 법.   
list.remove(x) : 리스트에서 첫 번째로 등장하는 x를 제거한다. 해당 값이 없으면 오류 발생.   
set(list) : 리스트에서 중복되는 요소를 제거한다.   
list[1:6]은 인덱스 1부터 5까지 슬라이싱 (6은 포함되지 않음)   
list[::-1] : 리스트를 역순으로 뒤집는다. 뒤에서부터 슬라이싱 한 것.   
sum(list)을 len(list)로 나누면 list의 평균이 된다.   

## 3. 반복문 250425 ~ 250427
입력이 많을 때는 input() 대신 sys.stdin.readline()을 쓰면 훨씬 빠르다. 특히 백준에서 많이 사용.   
for문에서 그냥 반복만 할 때는 i보다는 _를 관례적으로 선호   

## 2. 조건문 250421 ~ 250425
all(val < x for val in list) : 리스트 안의 모든 요소가 < x 를 만족하는 조건   

## 1. 입출력과 사칙연산 250416 ~ 250420
list[-i] : 뒤에서부터 i번째 인덱스   
map(int, input().split()) : 리스트에 int를 전부 적용한다.   
sum(list) : list의 모든 요소들의 합. sum()안에는 다양한 것들이 들어간다.   
문자열을 """으로 묶으면 줄바꿈을 유지할 수 있다.   
문자열 안의 백슬래시 \는 이스케이프 문자이기 때문에 조심해서 써야 한다. 예: \\n은 줄바꿈이 되고, \\로 써야 실제 \가 출력된다.   