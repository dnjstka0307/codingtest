nums, hand = map(int, input().split())
lists = list(map(int,input().split()))
minus = []
plus = []

for i in lists:
    if i < 0:
        minus.append(-i)
    else:
        plus.append(i)
minus.sort()
plus.sort()   

total = []
for i in range(len(plus)//hand):
    total.append(plus[-((i)*hand +1)])
if len(plus)%hand != 0:
    total.append(plus[-((len(plus)//hand)*hand +1)])
    
for i in range(len(minus)//hand):
    total.append(minus[-((i)*hand+1)])
if len(minus)%hand != 0:
    total.append(minus[-((len(minus)//hand)*hand +1)])

print(max(total) + (sum(total) - max(total))*2)

# 풀이 생각 : 음양으로 나누기 ~ 큰 값부터 hand만큼 간다면 결국 움직이는 거리는 몇개를 가져가던 최대거리
# hand개 이하는 그것 끼리 계산
# 돌아올 필요 없으니 음양 전체에서 가장 먼 거리는 편도, 나머진 hand 초기화를 위해 왕복

# hand개를 옮길때 결국 움직이는 거리는 최대거리하나로 계산이 가능하다는 점 + 이를 슬라이싱으로 해볼 수 있다는 점