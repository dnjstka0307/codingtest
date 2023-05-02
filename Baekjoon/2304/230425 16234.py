from collections import deque 

n, l, m = map(int,input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
def bfs(graph,n,l,visit,m,x,y):
    que = deque()
    now = deque()
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
        return 0, now
    else:         
        return int(total/len(now)), now

ans = 0    
while True:
    avgs = []
    visit_list = []
    visit = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visit[y][x] == 0:
                avg, visits = bfs(graph,n,l,visit,m,x,y)
                if avg != 0:
                    avgs.append(avg)
                    visit_list.append(visits)         
    if avgs:
        for i in range(len(avgs)):
            for x,y in visit_list[i]:
                graph[y][x] = avgs[i]
        ans += 1
    else:
        break
    
print(ans)

# 풀이 생각 : bfs를 이용해서 탐색을 하는 것은 같으나, 한 bfs가 수행되고 결과를 실행하는 것이 아니라, 전체를 bfs로 탐색후에 그제서야 결과값을 실행하고 루프를 돌아야 함
# 그래서 결과값을 bfs마다 저장후 그래프 전체를 순회한 뒤에 결과값에 대한 액션 진행

# 마지막 코드단에서 for중첩이 상당히 되는데 조금더 깔끔하게 진행을 할 수는 없을까