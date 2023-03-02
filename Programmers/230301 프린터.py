# 풀이 생각 : deque로 location의 문서가 출력될 때까지 돌려보기

from collections import deque
def solution(prior, location):
    prior = deque(prior)
    ans = 0
    while True:
        if location != 0:
            if prior[0] < max(prior):
                prior.rotate(-1)
            else:
                prior.popleft()
                ans += 1
            location -= 1
        else:
            if prior[0] < max(prior):
                prior.rotate(-1)
                location = len(prior)-1
            else: 
                ans += 1
                break
    return ans

# 반복문 사용이 아닌, location 기준 앞뒤 문서들의 값들을만 갖고 컴팩트하게 쓸수있지 않을까