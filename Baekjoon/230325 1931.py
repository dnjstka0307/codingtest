nums = int(input())
tmp = []
for i in range(nums):
    tmp.append(list(map(int,input().split())))
               
tmp = sorted(tmp, key=lambda x : x[0])
tmp = sorted(tmp, key=lambda x : x[1]) 
               
last = -1
ans = 0
for i in tmp:
    if i[0] >= last:
        last = i[1]
        ans+=1
               
print(ans)

# 풀이 생각 : 시작순으로 sort후 종료순으로 sort를 하게 되면, 시작순서가 빠르면서 또 같은 시작순서내에선 종료가 빠른 것이 먼저오게 sort
# 이를 이용해서 앞에서부터 그냥 시작과 끝을 비교해가며 +1

# sort 두번에 전체 리스트 조회를 하기에 시간복잡도가 상당히 높고, 실제로 시간소요도 많이된다
# 다른 sort를 사용하지 않는 다른 방법이 있을까