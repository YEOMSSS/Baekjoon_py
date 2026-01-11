백준 단계별로 (12단계까지) 완료

알고리즘 강의(기초부터 중급까지) 문제 풀기  
기초1, 기초2 완료  
중급1 진행중  
중급2, 중급3 예정

시간제한이 걸리면 PyPy3으로 제출.  
같은 코드를 PyPy3으로 제출하면 메모리를 python3보다 두배로 먹긴 해도, 두배 빨라진다.  
PyPy3으로 dfsR 재귀 빡세게 돌리면 메모리 초과가 난다. 이때는 python3로.

정렬문제나 그래프문제는 python으로 풀게 되는 감이 있다.  
나머지는 오히려 c언어가 편한 거 같은데 말이지.  
2-2학기 끝: 뭔 개소리야? 파이썬은 신이다.

# 00. 기타

solved.ac에서 마라톤이나 CLASS를 푼 찌꺼기들

#### itertools.groupby(string)

groupby는 연속으로 같은 값들을 묶어주는 함수다.

    for ch, group in groupby(string):
    print(ch, list(group))

#### dict.get(key, default)

key가 dict에 있으면 value 반환, 없으면 default 반환

#### Counter 모듈 most_common

dictionary 형태로 작동한다. most_common을 Counter에 사용하면 빈도순으로 출력된다.

    word_counter = Counter(words)
    print(word_counter.most_common(3))

    Counter({'python': 3, 'is': 3, 'amazing': 1, 'and': 1, 'fun.': 1, 'powerful.': 1})
    [('python', 3), ('is', 3), ('amazing', 1)]

#### min(list, key=함수)

    words = [input().rstrip() for _ in range(n)]

    # 비교할 때만 소문자로 비교됨.
    # min(list)는 list에서 가장 작은 값을 반환하지?
    # min(list, key=함수)를 하면 비교 기준이 함수가 되어 가장 최솟값을 반환한다.
    # 여기서는 문자열이니까 아스키코드 기준으로 비교하게 되는거임.
    word_min = (min(words, key=lambda x: x.lower()))

#### bit_count(), bit_length()

2진수로 바꿨을 때 1의 개수를 세주는 n.bit_count()  
2진수로 바꿀 때 필요한 비트의 개수를 알려주는 n.bit_length()

#### 파이썬 슬라이싱 인덱스

파이썬에서 슬라이싱으로 인덱스를 가져올 땐 인덱스가 초과되어도 괜찮다.  
다만 단일 인덱스로 가져올 땐 주의.

`if s == t[i : i + len_s]:` 이런거에선 i + len_s가 len(t)를 뚫어도 괜찮지만
`if s == t[i + len_s]:` len(t) - 1 보다 크면 인덱스에러가 난다.

#### math.comb & math.perm

comb(N, M)은 nCm이고 (N개중에 M개선택한 조합의 수)  
perm(N, M)은 nPm이다 (N개중에 M개선택한 순열의 수)

#### string.replace('a', 'b')

string에서 a를 b로 바꿔주는 문자열 method.  
.replace는 무한이 뒤에 이어붙여 순차적으로 적용할 수 있다.

#### pow() 분할정복

실버 1629번 참고  
pow(x, y) 는 x ** y 를 겁나 빠르게 반환한다.  
pow(x, y, z) 는 x ** y % z 를 겁나 빠르게 반환한다.

#### math.sqrt(), math.isqrt()

제곱근을 반환한다. 차이는 isqrt는 소수점 이하를 자른다.  
isqrt는 int(sqrt)와 달리 부동소수점 오차를 걱정할 필요가 없어 효율적. 아예 int 형태로 반환함  
큰 수의 제곱근의 정수 부분만 정확하게 필요한 경우 주로 사용한다고 생각하면 된다.

#### dict.values()

딕셔너리에서 key와 value중 value만 모아 리스트처럼 동작하는 뷰 객체로 만든다.

#### collections.Counter

iterable을 넣으면 딕셔너리 형태로 개수를 세 준다.

#### \*을 이용한 변수 언패킹

    a, *b = [10, 20, 30]
    a = 10, b = [20, 30]

    *a, b = [10, 20, 30]
    a = [10, 20], b = 30

    a, *b, c = [10, 20, 30, 40]
    a = 10, b = [20, 30], c = 40

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

`words.sort(key=len)` # 길이 기준 정렬  
`words.sort(key=str.lower)` # 대소문자 무시 알파벳 정렬  
`words.sort(key=lambda x: (len(x), x))` # 길이 우선, 알파벳 보조 정렬

`words.sort(reverse=True)` # 기본 비교 기준의 역순  
`words.sort(key=len, reverse=True)` # 길이 기준 내림차순

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

# 04. 알고리즘 중급 1/3 250708 ~

## 712. 그리디 알고리즘 (도전) 260110 ~

## 711. 그리디 알고리즘 (연습) 260107 ~ 260108

슬슬 다시 속도가 올라온다. 한 학기가 지나니까 확실히 아는게 늘었다.

#### deque에 대하여

deque는 연결리스트 베이스로 만들어져 있어서 슬라이싱이 불가능하다.  
deque.reverse()를 통해 뒤집을 수 있다. 또는 1회성으로 reversed(deque)도 가능하다.

## 710. 그리디 알고리즘 250901 ~ 260106

c언어도 이제 해야하는데. 자바도 해야하는데. shit!  
그리디부터는 개강 하고서 하던지 해야겠구만. 내일부턴 c언어를 하자.

26.01.01. 학점 4.5를 받고 중급1에 돌아온 나. 내가 돌아왔다.

#### import heapq

파이썬에서 최소 힙과 최대 힙을 사용할 수 있게 하는 모듈이다.  
힙 전용 자료구조가 있는 것이 아니므로 `max_heap = []` 로 둔 리스트를 힙 규칙으로 관리한다.  
파이썬의 heapq는 최소 힙만 다루므로 최대 힙을 사용하고 싶다면 -를 붙여 쓰면 된다.

    최대 힙을 사용하는 경우
    max_heap = []
    heapq.heappush(max_heap, -value) # 힙에 value를 push한다.
    print(-heapq.heappop(max_heap)) # 힙의 최댓값을 pop한다.

#### zip(\*list)

list의 원소들이 열 기준으로 묶인다.

#### from bisect

bisect는 이진탐색으로 들어갈 위치를 찾아주는 모듈이다.  
bisect_right(a, x), bisect_left(a, x). 각각 정렬된 a에서 x가 들어갈 수 있는 위치를 찾는다.  
right는 들어갈 수 있는 가장 오른쪽 인덱스를, left는 들어갈 수 있는 가장 왼쪽 인덱스를 반환한다.

    a = [1, 3, 3, 5]
    bisect.bisect_left(a, 3)  # 1, [1, |3, 3, 5]
    bisect.bisect_right(a, 3)  # 3, [1, 3, 3, |5]

insort_left(a, x), insort_right(a, x)는 a에서 x로 각각 left, right한 위치에 x를 삽입까지 해준다.

#### XOR 연산 ^

a ^ b는 a와 b가 같으면 0, 다르면 1을 반환한다.  
2진수에서 bit ^= 1을 사용하면 bit가 0이면 1, 1이면 0을 반환하여 토글효과를 준다.

## 611. BFS (연습) 250722 ~ 250816

장기전이다. 이 꽉 물고 달리자. 많이 놀았네. 29일인데 이제 다섯 문제라니...  
이 씨발 거의 3주를 이거만 잡고있었네. 진짜 레전드네. 의욕을 가지라고. 열심히 하란 말이야.  
그래도 골드 하위 bfs 정도는 이젠 밥 먹듯이 풀 수 있어. 쉽다, 쉬워.

#### input().split()

자동으로 리스트 형태로 저장된다.  
list(map(int, input().split()))에서 list를 쓰는 이유는 map 때문일 뿐이다.

#### tuple을 정렬할 때

sorted((X, Y, Z))는 작동하지 않는다.  
tuple(sorted([X, Y, Z]))를 사용하도록 하자.

## 541. 브루트 포스 - 비트마스크 (연습) 250717 ~ 250719

#### set.union(iterable)

set에 있는 합집합 만들기 코드.  
리스트의 +연산 느낌인데, 모든 iterable을 커버 가능하다.

## 533. 브루트 포스 - 재귀 (참고) 250716 ~ 250716

#### @lru_cache(maxsize=None)

재귀함수 def 바로 위에 이 한줄을 써주면 중복연산을 없애준다.  
한번 했던 계산을 캐시로 저장해 다시 안하고 불러오는 소중한 한 줄이다.  
@lru_cache는 "DP 테이블 없이 DP를 구현할 수 있는 방법"이다.  
Top-down 방식으로 상태만 정의하면 끝. 없이도 코드를 완성할 수 있어야 한다.

## 531. 브루트 포스 - 재귀 (연습) 250709 ~ 250716

길었다. 너무길었는데... 다음엔 더 짧게 할 수 있도록 해보자. 어려웠다.

## 521. 브루트 포스 - 순열 (연습) 250708 ~ 250709

#### zip()

**여러 iterable(리스트 등)**을 병렬로 묶어서 쌍을 만들어주는 함수

    a = ['A', 'B', 'C']
    b = [9, 8, 7]

    z = zip(a, b)
    print(list(z))  # [('A', 9), ('B', 8), ('C', 7)]

#### list.extend()

list.append()와 달리 리스트를 풀어서 하나씩 집어넣는다. 병합느낌.

#### set.update(iterable)

set.add()와 달리 여러개를 set에 전부 집어넣을 수 있다.

#### 딕셔너리의 정렬

dict.items()를 이용한다.  
`sorted_items = sorted(visited.items(), key=lambda x: x[1], reverse=True)`
이건 값(value) 기준 내림차순 정렬이다.

# 03. 알고리즘 기초 2/2 250608 ~ 250707

## 620. 트리 1 250705 ~ 250707

트리는 DFS 방식의 순회를 사용한다. 전위, 중위, 후위가 대표적이다.
213_1991번 문제 참고. 개념적으로 도움되는 문제.

#### 이진 트리

각 노드가 최대 두 개의 자식 노드를 가지는 트리 구조.  
루트(Root) 트리의 맨 위 노드 (시작점)  
부모(Parent) 다른 노드를 가리키는 노드  
자식(Child) 부모에게 연결된 노드  
리프(Leaf) 자식이 없는 노드 (끝 노드)  
서브트리(Subtree) 어떤 노드를 루트로 가지는 하위 트리  
깊이(Depth) 루트에서 해당 노드까지의 거리

#### 전위 순회 preorder

순서: 루트 → 왼쪽 → 오른쪽

    def preorder(node):
        if node:
            print(node.value)         # 1. 루트 처리
            preorder(node.left)       # 2. 왼쪽 서브트리 순회
            preorder(node.right)      # 3. 오른쪽 서브트리 순회

#### 중위 순회 inorder

순서: 왼쪽 → 루트 → 오른쪽

    def inorder(node):
        if node:
            inorder(node.left)        # 1. 왼쪽 서브트리 순회
            print(node.value)         # 2. 루트 처리
            inorder(node.right)       # 3. 오른쪽 서브트리 순회

이진 탐색 트리(BST)의 경우, 중위 순회를 하면 오름차순 정렬된 결과가 나옴.

#### 후위 순회 postorder

순서: 왼쪽 → 오른쪽 → 루트

    def postorder(node):
        if node:
            postorder(node.left)      # 1. 왼쪽 서브트리 순회
            postorder(node.right)     # 2. 오른쪽 서브트리 순회
            print(node.value)         # 3. 루트 처리

## 610. BFS 250703 ~ 250705

#### 0-1BFS

이 알고리즘은 간선의 가중치가 0 또는 1인 그래프에서 작동하기 때문에 0-1BFS라고 불립니다.  
간선의 가중치가 0 또는 1인 임의의 정점 u에 BFS를 실행해봅시다.

## 602. 그래프 1 (도전) 250701 ~ 250702

dfs, dfsR, bfs. 검증.

## 601. 그래프 1 (연습) 250629 ~ 250630

## 600. 그래프 1 250624 ~ 250629

194번 dfs와 bfs https://www.youtube.com/watch?v=_hxFgg7TLZQ

#### 이분 그래프

인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프.
https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html

#### sys.setrecursionlimit(10\*\*6)

파이썬에서는 기본적으로 재귀 깊이가 1000까지로 설정되어 있다.  
깊이가 1000을 넘어가면 런타임 에러 (RecursionError)가 뜨기 때문에, setrecursionlimit으로 늘려줘야 한다.
셋-리커전-리밋. 재귀한계설정이라고 생각하면 되겠다. 10000정도가 적당한 듯.  
10\*\*6이면 웬만한 채점기는 다 뚫린다.

#### 연결 요소

그래프 한개라고 줘 놓고는 여러 component로 뚝뚝 떨어진 그래프들이 있을 수 있는데,
1-2-5-1 3-4-6 처럼 나누어진 각각의 그래프를 연결 요소라고 한다.

#### 그래프

그래프(Graph)란 노드(Node)와 간선(Edge)으로 연결관계를 표현하는 자료구조이다.  
노드는 정점(Vertex)라고 불리기도 한다.

#### DFS

DFS 알고리즘은 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.  
DFS는 stack으로 구현한다. 일단 첫 노드를 스택에 넣음으로서 탐색이 시작된다.  
스택의 top을 pop해서 프린트하고 top의 자식노드를 전부 집어넣는다.  
그리고 또 pop해서 프린트하고 그것의 자식노드를 다 넣고... 무한 반복해서 전부 탐색한다.

dfs는 재귀호출로도 나타낼 수 있다. 백트래킹은 dfs의 일종이다.

#### BFS

BFS 알고리즘은 너비 우선 탐색. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다.  
BFS는 queue(deque)로 구현한다. 일단 첫 노드를 큐에 넣음으로서 탐색이 시작된다.  
큐를 popleft해서 프린트하고 그것의 자식노드를 다 집어넣는다. 무한 반복해서 전부 탐색한다.

## 540. 브루트 포스 (비트마스크) 250621 ~ 250624

#### mask.bit_count()

192번 참고. 보통 비트를 이용해 combinations의 역할을 할 때 사용한다.
마스크에 비트가 몇 개 켜져있는지를 반환하는 함수. 아래 두 함수는 같은 의미다.

    team_mask = [mask for mask in range(1 << N) if mask.bit_count() == N // 2]
    N비트 마스크에 비트가 N//2개 켜져있으면 리스트에 넣는 코드이다.

    team_mask = []
    for mask in range(1 << N):
        if bin(mask).count("1") == N // 2:
            team_mask.append(mask)

#### 비트와 조합론

비트를 이용해서 내장함수나 백트래킹의 역할을 대신할 수 있다.  
range(1, 1 << N)은 스위치 N개로 만들수 있는 조합의 수이다. (공집합 제외)  
N=3이면, range(1, 8)이고 001, 010, 011, 100, 101, 110, 111이 나온다.  
이걸 리스트의 인덱스로 사용해서 perm이나 comb를 만드는 데에 사용할 수 있다.

#### 메모리 초과가 날 때

비트마스크로 해도 메모리 초과가 난다면, 입력을 어떻게 받고 있는지 한번 보자.  
백준에서 채점을 할 때는 한 번에 입력받는것보다, 한 줄씩 입력을 읽고 바로 처리하는 구조가 메모리 초과가 안 난다.

sys.stdin.read()는 입력 전체를 한 번에 메모리에 올려버립니다.  
백준처럼 M ≤ 1,000,000까지 입력이 올 수 있는 경우 → 메모리 4MB 제한에서 read + splitlines로 초과될 수 있음  
sys.stdin.read() + splitlines()는 백준에선 위험 (메모리 초과 유력)

#### 진수 표시 (2진수, 8진수, 16진수)

bronze 2 11816번 참고
2진수: bin(13) == 0b1101  
8진수: oct(15) == 0o17  
16진수: hex(31) == 0x1f

#### 비트마스크와 비트 연산 기호

190_11723 문제 참고

    비트 연산 설명:
    1 << k: k번째 비트를 켠다 (0부터 시작)
    | : OR → 하나라도 1이면 1 (켜기용)
    & : AND → 둘 다 1이면 1 (끄기용)
    ^ : XOR → 다르면 1 (반전용)
    ~ : NOT → 비트 반전
    (1 << 20) - 1 → 20비트 전부 1 (모두 켜기)

## 530. 브루트 포스 (재귀) 250616 ~ 250620

#### it = iter(iterable), next

189_1248 문제 참고

#### set에서의 뺄셈

list + list는 가능하지만, list - list는 불가능하다.  
요소끼리 빼고 싶다면 set으로 변환하여 set - set을 하면 된다.

#### DFS

모든 경우의 수를 전부 살펴본다는 점에서 브루트포스와 같다.  
그러나 DFS는 트리를 따라 최대 깊이로 탐색한다는 점에서 다르다.  
모든 백트래킹은 DFS 방식의 탐색을 이용한다.

#### nonlocal variable

밖 함수에서 선언된 variable의 값을 함수 내에서 변경하고 싶다면 함수가 시작할 때 global variable을 한번 써주면 된다.

## 520. 브루트 포스 (순열) 250614 ~ 250615

#### unpacking 문법 요약

`k, *arr = map(int, input().split())`  
\*arr은 "나머지 값을 unpack해서 리스트로 만들어줘" 라는 뜻  
3 1 2 3을 입력받아서 3, [1, 2, 3]으로 반환한다.

`a, b = [1, 2]` 일반적인 unpacking a = 1, b = 2
`a, *b = [1, 2, 3, 4]` 나머지 전부 리스트로 a = 1, b = [2, 3, 4]
`*a, b = [1, 2, 3]` 앞쪽 전부 리스트로 a = [1, 2], b = 3
`a, *b, c = [1, 2, 3, 4, 5]` 양쪽 값을 분리 a = 1, b = [2, 3, 4], c = 5

#### global variable

밖에서 선언된 variable의 값을 함수 내에서 변경하고 싶다면 함수가 시작할 때 global variable을 한번 써주면 된다.

## 510. 브루트 포스 (N과 M) 250611 ~ 250614

주로 백트래킹에 대해 다루는 부분이다.

#### range(start, end)

start부터 end-1까지의 수를 반환하는 iterable이다. 리스트가 아니다.  
range 타입으로, 숫자들을 미리 저장하는 것이 아니라 필요할 때 값을 생성하는 방식으로 동작한다.

#### itertools.permutations(iterable, num)

iterable에서 서로 다른 요소 중 num개를 선택하는 **순열**을 중복 없이 **튜플** 형태로 생성한다.

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

10진수 -> 2진수 bin(255)[2:] # '11111111'  
10진수 -> 8진수 oct(255)[2:] # '377'  
10진수 -> 16진수 hex(255)[2:] # 'ff'

#### extend([a, b])

리스트를 풀어서 요소별로 추가 (평탄화)
append(a); append(b) 와 동일한 효과지만 한 번에 처리할 수 있다.

## 300. 수학 1 250520 ~ 250521

#### 최대공약수와 최소공배수 찾기

최대공약수(a, b) _ 최소공배수(a, b) = a _ b 이다.  
math.gcd(a, b) 는 최대공약수를 찾는다.  
math.lcm(a, b) 는 최소공배수를 찾는다.

- 유클리드 호제법  
  a와 b의 대소에 상관없이 a, b = b, a % b 를 반복해서 b가 0일 때 a가 최대공약수이다.

#### 에라토스테네스의 체

소수의 목록을 구해야 할 때 자주 사용한다. ~N 까지 소수의 목록을 구할 때

    sieve = [True] * (N + 1) # 0이 포함이므로 +1
    sieve[0] = sieve[1] = False # 0, 1은 소수가 아니다.

    for i in range(2, int(N ** 0.5) + 1): # 약수를 생각해보면 제곱근을 하는 이유를 알 수 있다.
        if sieve[i]:
            for j in range(i * i, N + 1, i): # 본인에 본인보다 작은 걸 곱한 경우는 이미 앞에서 처리했으니 제곱한다.
                sieve[j] = False

이런 식으로 코드를 짜면 sieve에서 True는 소수인 인덱스에만 남게 된다.  
i 씩 건너뛰면서 리스트를 False로 바꾼다는 것은, i 의 배수를 지운다는 것이다.  
i \* i 미만인 i 의 배수들은 이전 반복에서 이미 지워져 있다.  
시간복잡도는 O(N log log N). 굉장히 빠른 편이다. 대충 O(3N) 정도?

#### list.insert(index, val)

insert(2, 3) → 인덱스 2에 3을 넣고, 기존 요소는 오른쪽으로 밀린다.

## 203. 자료구조 1 (참고) 250518 ~ 250519

#### print(f"{value:.2f}")

value를 소수점 둘째 자리에서 반올림해서 f-string 방식으로 출력

#### 알파벳의 판정법

- char.isupper() : 대문자인지 판정
- char.islower() : 소문자인지 판정
- char.isalpha() : 알파벳인지 판정

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

print(\*list, sep= "") : 리스트의 요소를 ""으로 나눠 출력한다.

- collections.deque : 양쪽 끝에서 삽입, 삭제가 가능한 큐. appendleft()와 popleft()를 사용할 수 있다.

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

- n이 10배, 100배로 늘어날때, 실행시간도 10배, 100배로 늘어나면 O(n)이라고 합니다.
- 같은 경우에 실행시간이 100배, 10000배로 늘어나면 O(n^2)이라고 합니다.
- 같은 경우에 실행시간이 +1, +2만큼 늘어나면 O(log(n))이라고 합니다.
- 같은 경우에 실행시간이 바뀌지 않으면 O(1)이라고 합니다.

O형 시간복잡도 표현은 최고차항만 표시된다. 어차피 밑으로는 떨거지니까.  
코딩이 아니라 수학을 하는 느낌이다, 뭔가 w같아.

## 10. 기하: 직사각형과 삼각형 250508 ~ 250510

float("inf"), float("-inf"): infinity는 어떤 수보다도 크기 때문에 초기값으로 자주 이용한다.  
arr[::2] : 슬라이싱이다. 배열을 처음부터 두 칸씩 뛰며 읽는다. 인덱스 0, 2, 4...  
arr[1::2] : 배열을 1번 인덱스부터 두 칸씩 뛰며 읽는다. 인덱스 1, 3, 5...

- list[start:stop:step]
- start: 시작 인덱스 (기본값은 처음부터)
- stop: 멈출 인덱스 (기본값은 끝까지)
- step: 건너뛰는 간격. 음수면 뒤에서 앞으로 (예시로, [::-1]은 리스트를 뒤집는다.)

sys.stdin.read() (또는 open(0).read()): 한 번에 모든 입력을 받을 때 적합. EOF까지 문자열로 읽어옴.  
list = [int(input()) for _ in range(cnt)] : 이러면 엔터로 구분되게 cnt번 입력받을 수 있다.

## 09. 약수, 배수와 소수 250507 ~ 250508

empty list는 False를, not empty list는 True를 return한다. if not list: 같은 게 가능함.  
솟수 판독기를 만들 땐 int(math.sqrt())를 사용해 제곱근까지만 판단하자. num \*\* 0.5 도 좋다.

- for - else 문법 : for 안에서 break 없이 모든 반복이 끝나면 else를 실행.  
  77번, 78번에서 소수 판정과 소인수분해 잘 알아두자.

## 08. 일반 수학 1 250505 ~ 250507

iterable : 보통 반복 가능한 객체를 의미한다. 리스트, 문자열, 튜플 등  
int(string, base) : string을 base진법으로 변환한다. 그냥 int(x)에는 ,10 이 생략되어 있는 것이다. 기본 10진수.

- math.ceil()은 올림, math.floor()는 내림.
- int()는 소수점 아래를 그냥 지움.
- round()는 반올림.

올림(x / y) == 내림(x − 1 / y) + 1

## 07. 2차원 배열 250504 ~ 250504

def matrix*maker(row): return [list(map(int, input().split())) for * in range(row)]  
result = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)] : 보기 좋은 코드  
[a, b, c] + [d, e] == [a, b, c, d, e] : 리스트끼리 더하면 합쳐진 리스트가 된다.  
a, b = divmod(c, d) : c // d == a, c % d == b  
"abcde"를 list(input())으로 받으면 ['a', 'b', 'c', 'd', 'e']가 된다.  
"abcde"를 list(input().split()) 으로 받으면 ["abcde"]로 저장된다. 공백 기준 구분이므로.

## 06. 심화 1 250502 ~ 250503

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

## 05. 문자열 250430 ~ 250502

문자열에는 리스트에서 사용하는 함수를 대부분 사용할 수 있다.  
string[] + string[] : 공백 없이 합쳐져 붙는다.  
ord(), chr() : 문자를 아스키코드로, 아스키코드를 문자로 바꾸는 함수. 이 둘을 이용하면 알파벳 리스트를 쉽게 만들 수 있다.  
print(sum([int(f) for f in input()])) : 그냥 보기 좋아서 넣었다.  
string.find(x)는 문자열 안에 x가 있으면 첫 인덱스를 반환하고, 없으면 -1을 반환한다.  
단, string.index(x)는 없을 경우 오류 발생.  
.strip()은 문자열의 앞뒤 공백을 제거한다. 사용 예시: input().strip().split()  
for char in string : 이런 식으로 리스트처럼 반복문을 사용할 수 있다. 한 글자씩 들어간다.

- input(EOF) -> EOFError 발생
- sys.stdin.readline(EOF) -> "" 빈 문자열 반환(32번 참고)
- sys.stdin.read(EOF) -> EOF 만난 시점까지 읽은 전체 입력 문자열로 반환

## 04. 1차원 배열 250428 ~ 250430

list.index() : 요소가 몇 번째 인덱스에 있는지 찾아준다.  
[0] \* 5 == [0, 0, 0, 0, 0] 리스트를 쉽게쉽게 만들자.  
list(range(1, 6)) == [1, 2, 3, 4, 5] 리스트를 케이크처럼 쉽게 먹는 법.  
list.remove(x) : 리스트에서 첫 번째로 등장하는 x를 제거한다. 해당 값이 없으면 오류 발생.  
set(list) : 리스트에서 중복되는 요소를 제거한다.  
list[1:6]은 인덱스 1부터 5까지 슬라이싱 (6은 포함되지 않음)  
list[::-1] : 리스트를 역순으로 뒤집는다. 뒤에서부터 슬라이싱 한 것.  
sum(list)을 len(list)로 나누면 list의 평균이 된다.

## 03. 반복문 250425 ~ 250427

입력이 많을 때는 input() 대신 sys.stdin.readline()을 쓰면 훨씬 빠르다. 특히 백준에서 많이 사용.  
for문에서 그냥 반복만 할 때는 i보다는 \_를 관례적으로 선호

## 02. 조건문 250421 ~ 250425

all(val < x for val in list) : 리스트 안의 모든 요소가 < x 를 만족하는 조건

## 01. 입출력과 사칙연산 250416 ~ 250420

list[-i] : 뒤에서부터 i번째 인덱스  
map(int, input().split()) : 리스트에 int를 전부 적용한다.  
sum(list) : list의 모든 요소들의 합. sum()안에는 다양한 것들이 들어간다.  
문자열을 """으로 묶으면 줄바꿈을 유지할 수 있다.  
문자열 안의 백슬래시 \는 이스케이프 문자이기 때문에 조심해서 써야 한다. 예: \\n은 줄바꿈이 되고, \\로 써야 실제 \가 출력된다.
