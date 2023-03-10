from collections import deque 
def solution(bridge_length, weight, truck_weights):
    now = deque([0 for i in range(bridge_length)])
    truck_weights = deque(truck_weights)
    ans = 0
    lens = 0
    weights = 0
    while len(truck_weights)!=0:
        x = now.popleft()
        if x!=0:
            lens-=1
            weights-=x
        if lens < bridge_length and weights+truck_weights[0] <= weight:
            n = truck_weights.popleft()
            now.append(n)
            ans += 1
            lens += 1
            weights += n
        else:
            now.append(0)
            ans += 1
    return ans + bridge_length

# 풀이 생각 : deque에 다리 위 트럭을 append pop하며 length와 weight를 확인하는 방법
# len나 sum을 사용할 경우 deque의 길이가 길어지면 시간복잡도의 문제가 있기에 따로 상수로 지정

# bridge_length의 길이를 갖는 deque를 생성하는 것이 효율적인가??
