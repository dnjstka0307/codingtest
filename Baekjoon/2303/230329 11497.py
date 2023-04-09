from heapq import *

case = int(input())
for _ in range(case):
    nums = int(input())
    woods = list(map(int, input().split()))
    
    heapify(woods)
    ans_0 = []
    ans_1 = []
    
    for i in range(nums):
        if i%2 == 0:
            x = heappop(woods)
            ans_0.append(x)
        else:
            x = heappop(woods)
            ans_1.append(x)
            
            
    ans = ans_0 + ans_1[::-1]
    
    diff = 0
    for i in range(nums):
        diff = max(abs(ans[i-1] - ans[i]), diff)
            
    print(diff)
    
# 풀이 생각 : 최소가 되는 배열 형태는, 표준평균분포의 꼴로 배열을 sort하면 됨 ~ heapq를 이용해서 배열을 만든 뒤 확인

# heapq를 이용해서 배열을 두개만들어서 합치는 형태가 아닌, 정렬 알고리즘 자체를 잘 쓴다면 더 빠르게 가능하지 않을까