# Baekjoon

백준 단계별로 (12단계까지)   
알고리즘 강의(기초부터 중급까지)문제 풀기   
기초1, 기초2, 중급1   

2025.05.13 100 solve 달성!!   

# 백준 단계별로 풀어보기 1 ~ 12
## 1. 입출력과 사칙연산 250416 ~ 250420
list[-i] : 뒤에서부터 i번째 인덱스   
map(int, input().split()) : 리스트에 int를 전부 적용한다.   
sum(list) : list의 모든 요소들의 합. sum()안에는 다양한 것들이 들어간다.   
문자열을 """으로 묶으면 줄바꿈을 유지할 수 있다.   
문자열 안의 백슬래시 \는 이스케이프 문자이기 때문에 조심해서 써야 한다. 예: \\n은 줄바꿈이 되고, \\로 써야 실제 \가 출력된다.   
## 2. 조건문 250421 ~ 250425
all(val < x for val in list) : 리스트 안의 모든 요소가 < x 를 만족하는 조건   
## 3. 반복문 250425 ~ 250427
입력이 많을 때는 input() 대신 sys.stdin.readline()을 쓰면 훨씬 빠르다. 특히 백준에서 많이 사용.   
for문에서 그냥 반복만 할 때는 i보다는 _를 관례적으로 선호   
## 4. 1차원 배열 250428 ~ 250430
list.index() : 요소가 몇 번째 인덱스에 있는지 찾아준다.   
[0] * 5 == [0, 0, 0, 0, 0] 리스트를 쉽게쉽게 만들자.   
list(range(1, 6)) == [1, 2, 3, 4, 5] 리스트를 케이크처럼 쉽게 먹는 법.   
list.remove(x) : 리스트에서 첫 번째로 등장하는 x를 제거한다. 해당 값이 없으면 오류 발생.   
set(list) : 리스트에서 중복되는 요소를 제거한다.   
list[1:6]은 인덱스 1부터 5까지 슬라이싱 (6은 포함되지 않음)   
list[::-1] : 리스트를 역순으로 뒤집는다. 뒤에서부터 슬라이싱 한 것.   
sum(list)을 len(list)로 나누면 list의 평균이 된다.   
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
continue : 그 자리에서 현재 반복을 멈추고, 다음 반복을 진행한다.   
## 7. 2차원 배열 250504 ~ 250504
def matrix_maker(row): return [list(map(int, input().split())) for _ in range(row)]   
result = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)] : 보기 좋은 코드   
[a, b, c] + [d, e] == [a, b, c, d, e] : 리스트끼리 더하면 합쳐진 리스트가 된다.   
a, b = divmod(c, d) : c // d == a, c % d == b   
"abcde"를 list(input())으로 받으면 ['a', 'b', 'c', 'd', 'e']가 된다.   
"abcde"를 list(input().split()) 으로 받으면 ["abcde"]로 저장된다. 공백 기준 구분이므로.   
## 8. 일반 수학 1 250505 ~ 250507
iterable : 보통 반복 가능한 객체를 의미한다. 리스트, 문자열, 튜플 등   
for index, value in enumerate(iterable) : index와 value에 iterable의 인덱스와 값이 들어간다.   
int(string, base) : string을 base진법으로 변환한다. 그냥 int(x)에는 ,10 이 생략되어 있는 것이다. 기본 10진수.   
* math.ceil()은 올림, math.floor()는 내림.   
* int()는 소수점 아래를 그냥 지움.   
* round()는 반올림.   
올림(x / y) == 내림(x − 1 / y) + 1   
## 9. 약수, 배수와 소수 250507 ~ 250508
empty list는 False를, not empty list는 True를 return한다. if not list: 같은 게 가능함.   
솟수 판독기를 만들 땐 int(math.sqrt())를 사용해 제곱근까지만 판단하자. num ** 0.5 도 좋다.   
* for - else 문법 : for 안에서 break 없이 모든 반복이 끝나면 else를 실행.   
77번, 78번에서 소수 판정과 소인수분해 잘 알아두자.   
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
## 11. 시간 복잡도 250510 ~ 250511
시간 복잡도의 개념이 11번번 폴더에 있는 time_complexity.md 파일에 잘 설명되어 있다. 밑으로 발췌   
* n이 10배, 100배로 늘어날때, 실행시간도 10배, 100배로 늘어나면 O(n)이라고 합니다.   
* 같은 경우에 실행시간이 100배, 10000배로 늘어나면 O(n^2)이라고 합니다.   
* 같은 경우에 실행시간이 +1, +2만큼 늘어나면 O(log(n))이라고 합니다.   
* 같은 경우에 실행시간이 바뀌지 않으면 O(1)이라고 합니다.   
O형 시간복잡도 표현은 최고차항만 표시된다. 어차피 밑으로는 떨거지니까.   
코딩이 아니라 수학을 하는 느낌이다, 뭔가 w같아.   
## 12. 브루트 포스 250511 ~ 250513
tuple : 변경할 수 없는 리스트. 소괄호로 감싸서 만든다.   
itertools.combinations(list, num) : list에서 서로 다른 요소 num개를 갖는 조합을 튜플로 생성한다.   
list = map(int, input().split()) : map() 은 이터레이터다. list를 한번 사용하면 증발한다.   
list = list(map(int, input().split())) : 이건 계속 사용할 수 있다.   
a, b = map(int, input().split()) : 얘는 이터레이터의 값이 a, b에 복제된 거라 계속 사용할 수 있다.   
numer(numerator) : 보통 분자의 변수명으로 사용.   
denom(denominator) : 보통 분모의 변수명으로 사용.   
sum(x > 10 for x in [5, 11, 20]) : 결과는 2다. sum 안에 있는 True를 1로 계산된다.   
