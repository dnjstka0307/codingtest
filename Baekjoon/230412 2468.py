from collections import deque
n = int(input())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def bfs(graph,x,y,n,visit,maxs,total):
    que = deque()
    que.append([x,y])
    visit[y][x] = True
    while que: 
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_+dx[i]
            ny = y_+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[ny][nx] > maxs and visit[ny][nx]==False:
                visit[ny][nx] = True
                que.append([nx,ny])
    
ans = 0
for i in range(101):
    total = 0
    visit = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[y][x] > i and visit[y][x]==False:
                bfs(graph,x,y,n,visit,i,total)
                total+=1
                
                
    ans = max(ans,total)
    
print(ans)


# 풀이 생각 : bfs를 이용해서, 특정값만 높은 인접 노드를 탐색, 한번의 bfs루프마다 total을 +1씩 해주면서 확인 ~ 즉 분리된 영역마다 +1, visit으로 이미 방문한 땅은 제외
# 100까지의 범위를 완전탐색하며 비교

# 만일 visit을 사용하지 않는다면, 한 영역이 영역에 포함된 크기만큼 반복되어 count되기에 visit을 이용해서
# 한번 방문한 영역은 조회하지 않도록 