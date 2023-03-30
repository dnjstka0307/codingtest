from heapq import * 
import sys

input = sys.stdin.readline

nums = int(input())
classes = []
last = []

for i in range(nums):
    time = list(map(int, input().split()))
    classes.append(time)
    
classes = sorted(classes, key=lambda x:x[0])


for i in range(nums):
    if i == 0:
        heappush(last, classes[i][1])
    else:
        if classes[i][0] < last[0]:
            heappush(last, classes[i][1])
        else:
            heappop(last)
            heappush(last, classes[i][1])
        
print(len(last))
    
# 풀이 생각 : 끝나는 시간을 저장, 만약 이어서 하게되면 대체 ~ heap을 사용해서

# classes도 heap으로 정렬해서 사용하고 싶은데 그러면 틀린다/? 오ㅐ