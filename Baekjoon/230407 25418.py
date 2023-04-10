start, end = map(int, input().split())

ans = 0
while True:
    if end==start:
        break
    if end%2 == 0 and end>=start*2:
        end = end//2
    else:
        end -= 1
    ans+=1

print(ans)    

# 풀이 생각 : 그리디로 end-to-start, 이때 무작정 //2하는 것이 아닌 두배이상일때만

# 계속 오류가 나서 예제로 확인해보니 7>8에서 7>4가 되는 문제~ 따라서 추가 조건확인
