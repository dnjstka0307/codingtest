from collections import deque
n = int(input())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    graph.append(list(input()))

def bfs_normal(graph,visit,x,y,n):
    que = deque()
    que.append([x,y])
    visit[y][x] = 1
    while que:
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visit[ny][nx] == 0 and graph[ny][nx] == graph[y_][x_]:
                visit[ny][nx] = 1
                que.append([nx,ny])
                
def bfs_weak(graph,visit,x,y,n):
    que = deque()
    que.append([x,y])
    visit[y][x] = 1
    while que:
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visit[ny][nx] == 0 and graph[y_][x_] in ('R','G') and graph[ny][nx] in ('R','G'):
                visit[ny][nx] = 1
                que.append([nx,ny])
            elif  visit[ny][nx] == 0 and graph[ny][nx] == graph[y_][x_]:
                visit[ny][nx] = 1
                que.append([nx,ny])
                
normal_ans = 0
weak_ans = 0
visit = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if visit[y][x] == 0:
            bfs_normal(graph,visit,x,y,n)
            normal_ans += 1
visit = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if visit[y][x] == 0:
            bfs_weak(graph,visit,x,y,n)
            weak_ans += 1
            
print(normal_ans, weak_ans)

# 풀이 생각 : 일반적인 경우엔 그냥 평범한 bfs, 색약인 경우에는 추가 조건을 달아줘서 bfs

# 어렵지는 않다..?