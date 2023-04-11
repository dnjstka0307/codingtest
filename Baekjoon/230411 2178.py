from collections import deque

n, m = map(int, input().split())
graph = [[0]*(m+1)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    g = [0]+list(map(int, input()))
    graph.append(g)

def bfs(graph, x, y, n, m):
    que = deque()
    que.append([x,y])
    while que:
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx < 0 or ny < 0 or nx > m  or ny > n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y_][x_]+1
                que.append([nx,ny])
            if nx == m and ny == n:
                break
                
bfs(graph,1,1,n,m)
print(graph[n][m])

# 풀이 생각 : 최단거리~bfs사용 ~ 어차피 bfs사용시 되돌아 올 일은 없기에 visit사용 필요  x, 무조건 이어져 있기에 끝까지 확인

# 만일 이어져 있지 않거나, 예외의 크기가 많이 커질 경우 시간이 상당히 소요되기에 n,m이 확인될때 break걸어주는 것도 고려