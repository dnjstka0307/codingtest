start, end = map(str, input().split())
ans = 1    
while start != end:
    if end[-1] == '1':
        end = end[:-1]
        ans+=1
    elif int(end)%2 == 0:
        end = str(int(end)//2)
        ans+=1
    elif int(end)%2 != 0:
        ans = -1
        break
        
    if end == '':
        ans = -1
        break
        
print(ans)       

# 풀이 생각 : start>end에서 가는 방향을 거꾸로 생각해서 end>start로 생각 ~예외사항으로 start가 공백이 되는 경우를 확인
# str를 안쓰고 int값으로만 -1 후 10으로 나눠주는 방식을 고려 할 수도 ? 이게 더 시간복잡도면에선 낫다

    