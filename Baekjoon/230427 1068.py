n = int(input())
lists = list(map(int, input().split()))
delete = int(input())
graph = {i:[] for i in range(n)}
for i in range(n):
    if lists[i] == -1:
        pass
    else:
        graph[lists[i]].append(i)
        
def dfs(graph,i):
    del_lists = graph.pop(i)
    for x in del_lists:
        dfs(graph,x)
        
dfs(graph,delete)
    

print(list(graph.values()).count([delete]) + list(graph.values()).count([]))  

# 풀이 생각 : 우선 grpah형태의 dict을 만든 뒤, dfs를 이용해 삭제해야하는 노드를 부모로 갖는 노드는 전부 삭제 ~ 어차피 dfs로 실시간 삭제가 되기에 visit의미없음
# 이때 자식노드(딕셔너리의 value)가 빈 리스트인 경우를 count
# 추가적으로 트리가 항상 이진트리가 아닐수도 있다는 반례가 있음 >> 즉 삭제해야하는 노드 하나만을 갖는 부모노드는 리프노드가 되기에 추가로 count

# 이러한 트리구조에 대해 이진트리라는 것이 명시가 안되어있고 반례가 필요하다면 그 외 트리 형태도 고려해보자