from itertools import permutations
def solution(numbers):
    lists = list(map(int, numbers))
    nums = []
    for x in range(1,len(lists)+1):
        for i in permutations(lists,x):
            num = ''
            for z in i:
                num+=str(z)
            if num[0] == '0':
                pass
            else:
                nums.append(num)
    ans = 0
    nums = set(nums)
    for i in [i for i in nums if i!='1']:
        check = 0
        for x in range(2,(int(i)//2)+1):
            if int(i)%x == 0:
                check += 1
                break
        if check == 0:
            ans += 1
                
    return ans

# 풀이 생각 : 정말 단순하게 모든 숫자들 조합을 확인 ~ 정수필터링 후 소수 찾기로 확인

# 무식하게 for문 돌리는 거라 시간초과의 문제가 있는데 개선의 여지가?