# Baekjoon

백준 단계별로 (12단계까지)   
알고리즘 강의(기초부터 중급까지)문제 풀기   
기초1, 기초2, 중급1   

## 1. 입출력과 사칙연산 250416 ~ 250420
list[-i] : 뒤에서부터 i번째 인덱스   
map(int, input().split()) : 리스트에 int를 전부 적용한다.   
sum(list) : list의 모든 요소들의 합. sum()안에는 다양한 것들이 들어간다.   
문자열을 """으로 묶으면 줄바꿈을 유지할 수 있다.   
문자열 안에 백슬래쉬\는 조심해서 사용한다.   
## 2. 조건문 250421 ~ 250425
all(val < x for val in list) : 리스트 안의 모든 요소가 < x 를 만족하는 조건   
## 3. 반복문 250425 ~ 250427
반복문에서 input을 쓸 때는 sys.stdin.readline()을 써주면 시간 초과가 안 난다.   
for문에서 그냥 반복만 할 때는 i보다는 _를 관례적으로 선호   
## 4. 1차원 배열 250428 ~ 250430
list.index() : 요소가 몇 번째 인덱스에 있는지 찾아준다.   
[0] * 5 == [0, 0, 0, 0, 0] 리스트를 쉽게쉽게 만들자.   
list(range(1, 6)) == [1, 2, 3, 4, 5] 리스트를 케이크처럼 쉽게 먹는 법.   
list.remove() : 리스트에서 요소를 제거한다.   
set(list) : 리스트에서 중복되는 요소를 제거한다.   
list[1 : 6] : list의 인덱스 1 ~ 5를 나타내는 리스트   
list[::-1] : 리스트를 역순으로 뒤집는다.   
sum(list)을 len(list)로 나누면 list의 평균이 된다.   
## 5. 문자열 250430 ~ 250502
문자열에는 리스트에서 사용하는 함수를 대부분 사용할 수 있다.   
string[] + string[] : 공백 없이 합쳐져 붙는다.   
ord(), chr() : 문자를 아스키코드로, 아스키코드를 문자로 바꾸는 함수. 이 둘을 이용하면 알파벳 리스트를 쉽게 만들 수 있다.   
print(sum([int(f) for f in input()])) : 그냥 보기 좋아서 넣었다.   
string.find() : string에 있는 문자면 인덱스를 반환하고 없으면 -1을 반환한다.   
.strip은 앞뒤 공백을 제거한다. 사용예시 : input().strip().split()   
for char in string : 이런 식으로 리스트처럼 반복문을 사용할 수 있다. 한 글자씩 들어간다.   
* input(EOF) -> EOFError 발생   
* sys.stdin.readline(EOF) -> "" 빈 문자열 반환(32번 참고)   
* sys.stdin.read(EOF) -> EOF 만난 시점까지 읽은 전체 입력 문자열로 반환   
## 6. 심화 1 250502 ~ 250503
zip : 튜플로 묶어 쌍으로 돌아가게 한다. 나중에 해볼 것.   
for i in list1 + list2 : i에 합쳐진 리스트의 요소가 순서대로 들어간다.   
max(), min() : 최댓값과 최솟값을 찾는다.   
list.replace(x, y) : x를 y로 바꾼다.   
list.count() : 리스트에 요소가 나온 횟수를 반환한다.   
string.upper() : string을 전부 대문자로 바꾼다.   
백슬래쉬\ 후 엔터를 치면 코드가 다음줄로 바로 이어지도록 줄바꿈이 가능하다.   
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
abcde를 list(input()) 으로 받으면 ["a", "b", "c", "d", "e"] 로 저장된다.
abcde를 list(input().split()) 으로 받으면 ["abcde"]로 저장된다. 공백 기준 구분이므로.
## 8. 일반 수학 1 250505 ~ 
iterable : 보통 반복 가능한 객체를 의미한다. 리스트, 문자열, 튜플 등   
for index, value in enumerate(iterable) : index와 value에 iterable의 인덱스와 값이 들어간다.   
int(string, base) : string을 base진법으로 변환한다. 그냥 int(x)에는 ,10 이 생략되어 있는 것이다. 기본 10진수.