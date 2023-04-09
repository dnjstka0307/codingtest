nums, lens = map(int, input().split())
water = []
for i in range(nums):
    water.append(list(map(int, input().split())))
water = sorted(water, key=lambda x : x[0])

ans = 0
last = 0
for i in water:
    i[0] = max(i[0], last)
    l_ = i[1]-i[0]
    counts = l_//lens   
    less = l_%lens    
    if less == 0:
        ans += counts
        last = i[1]
    else:
        ans+=counts+1
        last = i[0]+(counts+1)*lens
print(ans)

# 그리디
# 풀이 생각 : 순서대로 sort한 뒤, 마지막 널빤지 위치를 다음 웅덩이 시작점과 비교하면서 진행
# 약간 지저분하게 진행된 거 같음 코드클린하게 짜는 습관필요 
        
