from itertools import permutations
def solution(k, dungeons):
    lens = len(dungeons)
    ans = 0
    lists = permutations(dungeons)
    for i in lists:
        counts = 0
        total = 0
        for x in i:
            if k-total >= x[0]:
                total+=x[1]
                counts+=1
            else:
                break
        if counts > ans:
            ans = counts
    return ans

# 풀이 생각 : permutation을 이용해서 완탐아닌 완탐을 하자, 단 전부 할 필요는 없고 최대크기인 permuatiaon 행들에 대해서만 진행하면된다
# 문제에선 해당되지 않지만 효율성 문제에서 permutation을 사용한다면 문제가 있을 수도