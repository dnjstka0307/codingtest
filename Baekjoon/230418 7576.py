from collections import deque

m, n = map(int, input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    lists = list(map(int, input().split()))
    graph.append(lists)
    
def bfs(graph,que,m,n):
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x]+1
                que.append([nx,ny])
                
   
 
que = deque()
for x in range(m):
    for y in range(n):
        if graph[y][x] == 1:
            que.append([x,y])
            graph[y][x] = 1
            
bfs(graph,que,m,n)

ans = 0
for i in graph:
    if 0 in i:
        ans = 0
        break
    else:
        ans = max(ans,max(i))
       
print(ans-1) 

# 풀이 생각 : bfs로 진행하나, 시작점이 여러개일 수 있고 또 동시에 bfs가 이뤄저야하기에 미리 deque에 시작점 여러개를 넣어 놓고 진행

# 어쨋든 bfs를 확인하기 위해선 직전 값을 +1 해야..