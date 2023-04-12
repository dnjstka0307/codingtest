from collections import deque
n, k = map(int, input().split())
visit=[0]*(100001)
def bfs(n,k):
    que = deque()
    que.append(n)
    while que:
        now = que.popleft()
        if now == k:
            print(visit[now])
            break
        for i in [now+1, now-1, 2*now]:
            if (0<=i<=100000) and visit[i] == 0:
                visit[i] = visit[now]+1
                que.append(i)
bfs(n,k)

# 풀이 생각 : bfs를 이용해서 뻗어 나가다가 만나게 되면 break

# bfs를 사용하는데 한번 루프를 돌때마다 count가 필요하다면 visit에 count값을 저장해놓고, bfs한 결과값의 visit위치에 +1해주는 것으로 해결해보자