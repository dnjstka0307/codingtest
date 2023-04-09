from collections import deque

edge, node, start = map(int, input().split())
graph = [[]]*(edge+1)
visit = [False]*(edge+1)



for _ in range(node):
    x, y = map(int, input().split())
    graph[x] = graph[x] + [y]
    graph[y] = graph[y] + [x]
    graph[x].sort()
    graph[y].sort()
    
def dfs(graph,visit,start):
    visit[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visit[i] == False:
            dfs(graph, visit, i)
    
def bfs(graph,visit,start):    
    que = deque()
    que.append(start)
    
    while que:
        now = que.popleft()
        if visit[now] == False:
            print(now, end=' ')
            visit[now] = True
            for i in graph[now]:
                que.append(i)           
    
dfs(graph,visit,start)
print()
visit = [False]*(edge+1)
bfs(graph,visit,start)

# 풀이 생각 : 기본 dfs bfs 문제