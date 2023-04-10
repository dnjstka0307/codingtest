def solution(genres, plays):
    dicts = {i :0 for i in set(genres)}
    lists = {i : [[0,0],[0,0]] for i in set(genres)}
    for i, (g, p) in enumerate(zip(genres, plays)):
        dicts[g] += p
        if p < lists[g][0][0] and p > lists[g][0][1]:
            lists[g][0][1] = p
            lists[g][1][1] = i
        elif p > lists[g][0][0]:
            lists[g][0][1] = lists[g][0][0]
            lists[g][0][0] = p
            lists[g][1][1] = lists[g][1][0]
            lists[g][1][0] = i
        elif p == lists[g][0][0]:
            lists[g][0][1] = p
            lists[g][1][1] = i
        else:
            pass
    _ = sorted(dicts.items(), key=lambda x : x[1], reverse=True)
    ans = []
    for i in _:
        if lists[i[0]][0][0] != 0:
            ans.append(lists[i[0]][1][0])
        if lists[i[0]][0][1] != 0:
            ans.append(lists[i[0]][1][1])
    
    return ans
# 풀이 생각 : 딕셔너리로 장르별 index와 play를 저장하는 방식

# 딕셔너리를 두개 사용하지 않고 두개로 끝낼 수 있을까?
# 조건문 남발 대신 컴팩트하게 끝낼 수 있을까?