'''
문제
그래프의 정점의 집합을 둘로 분할하여,
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

제한
2 ≤ K ≤ 5
1 ≤ V ≤ 20,000
1 ≤ E ≤ 200,000
예제 입력 1 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
예제 출력 1 
YES
NO
'''
# dfs로 탐색해서 같은색이 연속으로 나오면 안됨
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

K = int(input())

for _ in range(K):
    
    V, E = map(int, input().split())

    # 전형적인 dfsR 알고리즘 짜기
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    answer = True

    color = ["hmm"] + [""] * (V)

    def dfsR(prev, node):
        global answer

        if node in visited:
            return
        if not answer:
            return    
        if color[prev] == color[node]:
            answer = False
            return
        
        visited.add(node)

        if color[prev] == "RED":
            color[node] = "BLUE"
        elif color[prev] == "BLUE":
            color[node] = "RED"
        else:
            if color[node] == "":
                color[node] = "RED"

        for neighbor in graph[node]:
            dfsR(node, neighbor)
        visited.discard(node)


    for i in range(1, V + 1):
        if answer:
            dfsR(0, i)
        else:
            print("NO")
            break
    else:
        print("YES")

'''
# 시간초과가 난다. 다시 해보자. 문자열 비교는 너무 오래걸린다.
# 연결요소끼리는 어떤 노드에서 시작해도 이분그래프 판정은 똑같이 나온다.
# discard로 방문을 취소해 재방문을 시킬 이유가 없다는 것이다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

K = int(input())

# 전형적인 dfsR 알고리즘 짜기
def dfs(node, c): # 현재 노드와 그 노드의 색
    # color를 이용해 visted의 역할까지 하는 중. 0이 아니면 방문한 노드임
    color[node] = c # 색상판에 색 집어넣기
    for neighbor in graph[node]:
        if color[neighbor] == 0: # 색 지정이 안된 노드라면
            if not dfs(neighbor, -c): # 현재 색의 반대 색 집어넣기
                return False
        elif color[neighbor] == c: # 색 지정이 돼있는데 현재 색과 같다면
            return False # 이분그래프가 아닌 것이다
    return True

for _ in range(K):

    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (V + 1)  # 0은 미방문, 1은 RED, -1은 BLUE
    answer = True # 아무 일 없이 dfs가 진행되면 계속 True일 것

    for i in range(1, V + 1):
        if color[i] == 0: # 연결요소가 하나가 아닐 수 있다.
            if not dfs(i, 1): # 1에 RED부터 칠하고 dfs실행
                answer = False
                break
            
    print("YES" if answer else "NO")