from collections import deque 

# n, l, r = 3, 5 ,50
# graph = [[50, 30, 20], [20, 40, 30], [20, 20, 30]]

# n, l, r = 3, 5 ,50
# graph = [[50, 40, 50], [50, 50, 50], [50, 50, 50]]

# n, l, r = 3, 5 ,50
# graph = [[50, 40, 50], [50, 50, 50], [50, 50, 50]]

# n, l, r = 4, 1, 9
# graph = [[96, 93, 74, 30], [60, 90, 65, 96], [5, 27, 17, 98], [10, 41, 46, 20]]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
    
def bfs(graph,n,l,m,x,y):
    que = deque()
    now = deque()
    visit = [[0]*n for _ in range(n)]
    que.append([x,y])
    now.append([x,y])
    visit[y][x] = 1
    total = graph[y][x]
    while que:
        x_,y_ = que.popleft()
        for i in range(4):
            nx = x_+dx[i]
            ny = y_+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            check = abs(graph[y_][x_] - graph[ny][nx])
            if (l<=check) and (check<=m) and (visit[ny][nx]==0):
                visit[ny][nx] = 1
                que.append([nx,ny])
                now.append([nx,ny])
                total += graph[ny][nx]
    if len(now) == 1:
        return 0
    else:        
        avg = int(total/len(now))
        for x,y in now:
            graph[y][x] = avg

    

ans = 0
for x in range(n):
    for y in range(n):
        ans += bfs(graph,n,l,m,x,y)
print(ans)