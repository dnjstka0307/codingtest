def solution(operations):
    que = []
    for t in operations:
        try:
            if 'I' in t:
                que.append(int(t.strip('I ')))
            if 'D' in t:
                if '-' in t:
                    que.pop(que.index(min(que)))
                else:
                    que.pop(que.index(max(que)))
        except:
            pass
    if len(que) == 0:
        ans = [0,0]
        return ans
    else:
        ans = []
        ans.append(max(que))
        ans.append(min(que))
        return ans
    
    # 풀이 생각 : 그냥 최소와 최대값을 찾아서 리스트에서 pop
    
    # heapq를 사용하는 것이 의도 + 예시 크기가 커지면 시간초과 예상 ~ heapq를 사용해보자 