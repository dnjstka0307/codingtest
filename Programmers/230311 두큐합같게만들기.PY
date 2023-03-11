from collections import deque
def solution(que1, que2):
    que1,que2 = deque(que1),deque(que2)
    t = len(que1)
    answer = 0  
    sum_1 = sum(que1)
    sum_2 = sum(que2)
    goal = (sum_1+sum_2)/2
    count = 0
    while que1 and que2 and count < 2*t: 
        if sum_1 < sum_2:      
            move = que2.popleft()
            que1.append(move)
            sum_1 += move
            sum_2 -= move
            answer += 1
            count += 1
        elif sum_1 > sum_2:
            move = que1.popleft()
            que2.append(move)
            sum_2 += move
            sum_1 -= move
            answer += 1
        else:
            return answer
    else:
        return -1
            
# 풀이 생각 : 두 개의 큐의 원소를 계속해서 넣고 빼고 해서 확인, 결국 한바퀴돌면 똑같기에 반만 돌았을때 예외처리

# 약간 하드코딩된 느낌이라 개선이 필요할까?