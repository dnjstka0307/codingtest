from collections import deque
import sys
input = sys.stdin.readline

y, x = map(int,input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(y):
    graph.append(list(input()))
    
def bfs(graph,s_x,s_y,x,y):
    que = deque()
    visit = [[0]*x for _ in range(y)]
    que.append([s_x,s_y])
    visit[s_y][s_x] = 1
    check = 0
    while que:
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_+dx[i]
            ny = y_+dy[i]
            if nx<0 or ny<0 or nx>=x or ny>=y:
                continue
            if visit[ny][nx]!=0 or graph[ny][nx]=='W':
                continue
            que.append([nx,ny])
            visit[ny][nx] = visit[y_][x_] + 1
            check = max(check, visit[ny][nx])
    return check

ans = 0
for s_x in range(x):
    for s_y in range(y):
        if graph[s_y][s_x] == "L":
            check = bfs(graph,s_x,s_y,x,y)
            ans = max(ans, check)
            
print(ans-1)

# 풀이 생각 : 모든 x,y좌표들에 대해 조건에 부합할 경우, bfs진행 해당 좌표에서 제일 먼 곳까지의 거리를 비교해 가장큰 것을 반환

# 1>9로 가나 9>1가나 동일한 것인데, 이런 과정을 배제하면 속도면에서 개선이 될 거 같다
# 제2의visit을 만들어서 제외시키기?