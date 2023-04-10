from collections import deque

def bfs(graph,x,y,m,n):
    dx = [1,1,1,0,0,-1,-1,-1]
    dy = [1,-1,0,1,-1,1,-1,0]
    que = deque()
    que.append([x,y])
    graph[y][x] = 0
    while que:
        x_, y_ = que.popleft()
        for i in range(8):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                que.append([nx,ny])
                
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    graph = []
    ans = 0
    for _ in range(y):
        lists = list(map(int, input().split()))
        graph.append(lists)

    for xi in range(x):
        for yi in range(y):
            if graph[yi][xi] == 1:
                bfs(graph, xi, yi, x, y)
                ans += 1
    print(ans)
    
# 풀이 생각 : 한 엣지에 대해 인접한 모든 엣지를 확인하는 것이니 bfs를 사용해보자 ~ 풀이 자체는 간단 

# 여전히 x,y의 변수가 함수내에서 중복되어 사용되어서 헷갈리는 문제가 있음