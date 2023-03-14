nums, lens = map(int,input().split())
lists = list(map(int, input().split()))

lists = sorted(lists)
start = lists[0]
ans = 1

for i in lists[1:]:
    if i-start < lens:
        pass
    else:
        start = i
        ans+=1
print(ans)

# 그리디
# 풀이 생각 : 시작지점-현재지점의 길이의 차이가 lens 미만이면 테이프 계속 사용, 이상이면 테이프하나 사용하고 시작지점 리셋

# 그리디는 간단하게 현재지점에서 최적의 행동을 해보면 쉽게 풀이 가능해진다