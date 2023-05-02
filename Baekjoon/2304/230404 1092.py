n_c = int(input())
crane = list(map(int, input().split()))
n_s = int(input())
stock = list(map(int, input().split()))

crane.sort(reverse=True)
stock.sort(reverse=True)
ans = 0
if max(crane) < max(stock):
    ans = -1
else:
    while stock:
        for c in crane:
            for s in stock:
                if c >= s:
                    stock.remove(s)
                    break
                continue
        ans += 1
        if stock == False:
            break
print(ans)

# 풀이 생각 : 우선 리스트들을 sort후, 크레인이 박스를 보면서 들수 있으면 박스제거 break, 다음 크레인이 박스 확인 ~ 이를 stock이 없을때까지 반복

# sort도 시간복잡도가 상당하고 모든 리스트를 조회하는 방식이다보니 시간복잡도의 문제가 상당하다...sort의 개선과 반복문및remove의 개선이 필요