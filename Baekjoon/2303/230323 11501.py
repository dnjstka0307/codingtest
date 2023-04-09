case = int(input())
for _ in range(case):
    day = int(input())
    price = list(map(int, input().split()))
    
    revenue = 0
    maxs = 0
    for i in price[::-1]:
        if maxs >= i:
            revenue += (maxs-i)
        else:
            maxs = i
            pass

    print(revenue)
    
    # 풀이 생각 : 배열을 거꾸로 보고, 미래 값이 최고점일때 파는 것을 반복
    # 시간초과가 아슬아슬한 거 같은데 더 빠르게 처리할 방법이 있을까? 