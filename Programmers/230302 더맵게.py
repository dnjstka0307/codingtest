from heapq import * 
def solution(scoville, K):
    heapify(scoville)
    ans = 0
    while scoville[0]<K:
        min1 = heappop(scoville)
        min2 = heappop(scoville)
        new = min1 + (min2*2)
        if len(scoville) == 1 and new < K:
            return -1
        heappush(scoville, new)
        ans +=1
    return ans

# 풀이 생각 : heapq를 사용해서 제일 적은 값들을 계속 빼고 넣고 하기

# 최소값 최대값이 반복되는 경우에는 heapq를 써보자