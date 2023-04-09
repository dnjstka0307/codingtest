l_ = int(input())
lens = list(map(int, input().split()))
cost = list(map(int, input().split()))

min = 1000000001 
ans = 0
len_ = 0
for i in range(l_-1):
    # 최소값보다 현재 값이 클 경우 ~ 즉 주유를 여기서 할 필요  x
    if cost[i] > min:
        len_ += lens[i]
    # 최소값보다 현재 값이 작을 경우 ~ 주유를 해야함
    else:
        ans += len_ * min 
        min = cost[i]
        len_ = lens[i]
        
ans += len_*min
        
print(ans)

# 풀이 생각 : 역대최저가와 현재도시의 가격을 비교, 역대최저가보다 비싸면 역대최저가로 주유한다는 의미로 거리 더하기
# 만일 역대최저가보다 싸면 최저가 갱신후, 이전최저가 정산해서 금액에 더하기

# ans와 len_을 안쓰고 풀이가 가능할까?