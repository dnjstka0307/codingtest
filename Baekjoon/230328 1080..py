y_, x_ = map(int, input().split())
my_matrix = []
ans_matrix = []
for _ in range(y_):
    my_matrix.append(list(map(int, list(input()))))
for _ in range(y_):
    ans_matrix.append(list(map(int, list(input()))))

    
def change(y,x):
    for y_ in range(y,y+3):
        for x_ in range(x,x+3):
            if my_matrix[y_][x_] == 1:
                my_matrix[y_][x_] = 0
            else:
                my_matrix[y_][x_] = 1

ans = 0
if (x_<3 or y_<3) and my_matrix != ans_matrix:
    ans = -1
elif (x_<3 or y_<3) and my_matrix == ans_matrix:
    ans = 0
else:
    for y in range(y_-2):
        for x in range(x_-2):
            if my_matrix[y][x] != ans_matrix[y][x]:
                change(y,x)
                ans+=1
       
    
if my_matrix != ans_matrix:
    ans = -1
    print(ans)
else:
    print(ans)
    
# 풀이 생각 : 3*3 행렬이 전체 행렬위를 움직이면서 바꾼다고 가정했을때, 이미 바꾼 곳을 또 바꿔야하는 경운, 죽엇다 깨어나도 정답행렬로 바꿀 수 없는 생각 

# 수학적인 테크닉이 조금 필요한 부분이라고 생각 