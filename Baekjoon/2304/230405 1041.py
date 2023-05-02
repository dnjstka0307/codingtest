n = int(input())
nums = list(map(int, input().split()))
_ = ['A','B','C','D','E','F']
dice = {i:x for i,x in zip(_,nums)}

one = min(nums) * ((n-2)*(n-1)*4 + (n-2)*(n-2))

two_lists = ['AD','AC','AB','AE','BC','BD','BF','CE','CF','DE','DF','EF']
two = 0
for i in two_lists:
    check = dice[i[0]] + dice[i[1]]
    if two == 0:
        two = check
    else:
        two = min(two, check)

three_lists = ['ABD','BDF','DEF','ADE','ABC','BCF','CEF','ACE']
three = 0
for i in three_lists:
    check = dice[i[0]] + dice[i[1]] + dice[i[2]]
    if three == 0:
        three = check
    else:
        three = min(three, check)

two = two * ((n-2) * 8 + 4)
three = three*4
if n == 1:
    print(sum(nums)-max(nums))
else:
    print(one+two+three)
    
# 풀이 생각 : 주어진 n에 대해 주사위의 면이 1개, 2개, 3개 보이는 경우의 갯수 확인 ~ 주사위 구조상 2면 3면의 경우 생각 ~ 해당 경우를 갖고 최소값 도출

# 단순 주사위의 면과 최소값을 구하는 건 어렵지 않았으나, n=1인 경우의 수를 생각하지 못함