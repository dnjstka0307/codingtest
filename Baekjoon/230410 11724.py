import sys
sys.setrecursionlimit(10 ** 6)
input =  sys.stdin.readline


edge, node = map(int, input().split())
graph =[[] for _ in range(edge+1)]
visit = [False for _ in range(edge+1)]
for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
def dfs(graph,visit,x):
    visit[x] = True
    for i in graph[x]:
        if visit[i] == False:
            dfs(graph,visit,i)

            
total = 0            
for i in range(1,edge+1):
    if visit[i] == False:
        dfs(graph, visit, i)
        total+=1    
    
print(total)

# 풀이 생각 : dfs로 모든 연결된 노드 조회 후 끝나면 ans +1, 방문하지 않은 나머지 노드에 dfs반복

# 풀이 자첸 간단한데 파이썬의 재귀깊이가 제한이 얕아서 문제 ~ 데이터 조건을 보고 최악의 경우 재귀가 얼마나 반복될지 확인해보고 bfs로 푸는 방법도 생각해봐야겠다