from collections import deque

n = int(input())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(graph,x,y,n):
    que = deque()
    que.append([x,y])
    graph[y][x] = 0
    house = 1
    while que:
        x_, y_ = que.popleft()
        for i in range(4):
            nx = x_+dx[i]
            ny = y_+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                que.append([nx,ny])
                house += 1

    return house

ans = 0
ans_list = []
for xi in range(n):
    for yi in range(n):
        if graph[yi][xi] == 1:
            house = bfs(graph,xi,yi,n)
            ans_list.append(house)
            ans += 1
            
print(ans)
ans_list.sort()
for i in ans_list:
    print(i)
    
# 풀이 생각 : 1인 노드 중에 인접한 노드중 1인 것을 bfs해서 확인 ~~ 

# 반복되는 bfs
