import sys
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    ans = 1
    nums = int(input())
    score = []
    for _ in range(nums):
        score.append(list(map(int, input().split())))
    score = sorted(score, key=lambda x : x[0])
    mins = score[0][1]
    for i in score[1:]:
        if i[1] > mins:
            pass
        else:
            mins = i[1]
            ans+=1
    print(ans)
    
# 풀이 생각 : 첫번째 조건을 sort하게되면, 무조건적으로 i번째 사람은 i번 이후사람들보다 첫번쨰 조건은 우수하다는 것으로 조건 pass
# 따라서 i번째사람은, i번 이전의 사람들과 두번째 시험을 비교, 더 성적이 좋아야 pass

# 시간초과가 계속나서 확인해보니, 최소값을 계속해서 list[:i]로 min을 줘서 연산이 게속되어서 문제
# 그냥 어지간한 min, max의 경우에는 연산최소화를 위해서 상수로 지정해놓는 것이 좋다