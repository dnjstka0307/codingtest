n = int(input())
lists = sorted(list(map(int, input().split())))
print(lists[((len(lists)-1)//2)])

# 풀이 생각 : 수학적인 부분을 생각해보면 간단하게 풀 수 있다. 무조건적으로 해당 위치는 좌우에 얼마나 많은 집이 있는지에 갈려있음
# 이때 예외 상황으로 중복인 것이 짝수이냐 홀수이냐에 걸리는데, 무조건 앞에 것을 해주면 되는 만큼 전체 len의 절반을 준다면 이를 갖게 됨

# 가끔은 알고리즘이 아니라 수학적인 부분도 잘 고려를 해봐야겠다