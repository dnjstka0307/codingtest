from heapq import *

num, case = map(int, input().split())
cards = list(map(int, input().split()))

heapify(cards)

for i in range(case):
    x = heappop(cards)
    y = heappop(cards)
    new = x+y
    heappush(cards, new)
    heappush(cards, new)
    
print(sum(cards))

# 풀이 생각 : 정답을 최소화 하기 위해선 최소값끼리만 계속 확인을 해야함 ~ heapq 절대사용을 해
# 최대값 혹은 최소값의 반복은 무조건 heapq 사용을 해