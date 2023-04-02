start = input()
end = input()

s_l = len(start)
while s_l != len(end):
    if end[-1] == "A":
        end = end[:-1]
    else:
        end = end[:-1][::-1]
else:
    if start == end:
        print(1)
    else:
        print(0)
        
# 풀이 생각 : 그리디의 전형적인 방법으로 end-to-start 방식 사용, 이때 확인할 것은 start와 end의 길이
# 같은 길이일때 무조건 같아야 바꿀수있는 경우

# 난이도 치곤 쉬운듯?