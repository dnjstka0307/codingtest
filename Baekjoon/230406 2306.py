nums_com = int(input())
case = int(input())
graph = [[]]*(nums_com+1)
visited = [False]*(nums_com+1)

for _ in range(case):
    x, y = map(int, input().split())
    graph[x] = graph[x] + [y]
    graph[y] = graph[y] + [x]
    
def dfs(graph, i, visited):
    visited[i] = True
    for x in graph[i]:
        if visited[x] == False:
            dfs(graph, x, visited)
dfs(graph, 1, visited)
print(sum(visited)-1)

# 풀이 방법 : 주어진 노드연결을 그래프형식으로 변환 후 dfs

# dfs나 bfs나 뭘 사용하건 상관 없는 문제