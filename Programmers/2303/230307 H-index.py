def solution(citations):
    maxs = max(citations)
    if maxs == 0:
        return 0
    for x in reversed(range(maxs)):
        more = len([i for i in citations if i >= x])
        print(x, more)
        if x <= more:
            return x
        
# 풀이 생각 : citations의 최대값부터 조회해서 인용 수 확인하기

# 딱히 정렬 문제는 아니고 단순 구현식으로 풀었는데 과연 정렬로 풀 방법이?