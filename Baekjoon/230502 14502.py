from itertools import combinations
from collections import deque 

n, m = map(int,input().split())
graph = []
wall_candi = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    graph.append(list(map(int,input().split())))
for x in range(m):
    for y in range(n):
        if graph[y][x] == 0:
            wall_candi.append([x,y])
wall_candis = combinations(wall_candi, 3)
            
def make_wall(graph,visit,n,m,candis):
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                visit[y][x] = 1
    for x,y in candis:
        visit[y][x] = 1
                
                
def bfs(visit,n,m,x,y):
    que = deque()
    que.append([x,y])
    visit[y][x] = 2
    while que:
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_+dx[i]
            ny = y_+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if visit[ny][nx] == 0:
                visit[ny][nx] = 2
                que.append([nx,ny])

ans = 0
for candis in wall_candis:
    visit = [[0]*m for _ in range(n)]
    make_wall(graph,visit,n,m,candis)
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 2:
                bfs(visit,n,m,x,y)
    check = sum(visit,[]).count(0)
    ans = max(check, ans)
    
print(ans)

# 풀이 생각 : 첫번째로 벽을 세우는 경우를 combination으로 구해서 visit에 벽을 새로 세우고, 그 visit에 대해 virus의 bfs를 실행, 벽도 바이러스도 없는 경우 count

# 0으로만 이뤄진 visit을 만들고 graph에서 존재하는 벽을 visit에 세우고, 새로운 벽도 visit에 세우는데 사실 graph를 deepcopy하면 되는 부분이라
# 바꿔서 제출해봤는데 오히려 실행시간이 늘어남?? >> n,m의 범위가 크지 않아서 오히려 deepcopy하는 것보다 graph를 조회하면서 벽을 가져오는 것이 더 빠른듯