from collections import deque

def bfs(graph,s_x,s_y,g_x,g_y,n):
    dx = [-2,-1,-2,-1,2,1,2,1]
    dy = [-1,-2,1,2,-1,-2,1,2]
    que = deque()
    que.append([s_x,s_y])
    graph[s_y][s_x] = 1
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[ny][nx] == 0:
              graph[ny][nx] = graph[y][x]+1
              que.append([nx,ny])
            
            if nx == g_x and ny == g_y:
                break

case = int(input())
for _ in range(case):
    n = int(input())
    graph = [[0]*n for x in range(n)]
    s_x, s_y = map(int, input().split())
    g_x, g_y = map(int, input().split())
    bfs(graph,s_x,s_y,g_x,g_y,n)
    print(graph[g_y][g_x]-1)
    
# 풀이 생각 : 전형적인 지점 도달을 위한 bfs 사용 ~ 어렵진 않고 체스 나이트의 움직임만 구현해주면 됨, 다만 이미 방문한곳은 제외위해 ==0 조건 추가

# 레벨에 비해 어려운 난이도는 아닌듯