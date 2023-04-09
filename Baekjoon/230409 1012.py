from collections import deque
case = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph,m,n,x,y):
    que = deque()
    que.append([m,n])
    graph[n][m] = 0
    while que:
        _x, _y = que.popleft()
        for i in range(4):
            nx = _x+dx[i]
            ny = _y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= x or ny >= y:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                que.append([nx, ny])             
                        

for _ in range(case):
    ans = 0
    x, y, k = map(int, input().split())
    graph = [[0]*x for i in range(y)]
    for i in range(k):
        x_, y_ = map(int, input().split())
        graph[y_][x_] = 1
        
    for m in range(x):
        for n in range(y):
            if graph[n][m] == 1:
                bfs(graph, m, n, x, y)
                ans += 1         
    print(ans)
    
    # 풀이 생각 : 특정 좌표와 인접한 것들을 모두 count and repeat ~ bfs사용
    
    # 변수명할당을 계속 헛갈리게 해서 오류 발생 ~ 변수명 할당에 대한 나름대로 규칙을 세우자 