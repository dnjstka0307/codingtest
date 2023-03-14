name = input()
lists = sorted([i for i in name])
lists = {i : name.count(i) for i in lists}
start=''
last = ''
ans = ''
last_ = False
for i in lists.items():
    if i[1]%2 == 0:
        start += i[0]*(i[1]//2)
    else: 
        if last == '':
            if i[1] == 1:
                last = i[0]
            else:
                start += i[0]*(i[1]//2)
                last += i[0]*(i[1]%2)
        else:
            last_ = True
            break

if last_:
    print('I\'m Sorry Hansoo')
else:
    ans = start + last + start[::-1]
    print(ans)
    
# 풀이 생각 : 팰린드롬을 위해선 문자열 count가 홀수인 것이 하나만 있어야 함, 이를 통해 count가 짝수인것과 홀수인것을 모아 합치기
# 저장되는 문자열이 많고 for문으로 두번이나 리스트를 만들기에 시간복잡도의 문제있음 + sort