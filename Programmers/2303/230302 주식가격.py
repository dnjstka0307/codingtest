def solution(prices):
    ans = []
    l = len(prices)
    
    for i in range(l):
        time = 0
        for x in range(i, l-1):
            if prices[i] <= prices[x]:
                time+=1
            else:
                break
        ans.append(time)
        
    return ans

# 풀이 생각 : 완전 탐색으로 i번째와 그 이후 값들을 비교해보자


# 문제의도는 stack이나 deque를 이용하는 것이었는데 적절한 방법이 있을까