st = input()

st_1 = st.split('-')
st_2 = []
for i in st_1:
    _ = i.split('+')
    a = sum(map(int, _))
    st_2.append(a)
    
ans = st_2[0] - (sum(st_2[:1]))
print(ans)

# 풀이 생각 : +,-로만 이뤄진 식에 괄호를 넣어 최소가 되게 하려면, -부호 뒤에 있는 모든 값들에 괄호를 쳐주면 된다 ~ split을 두번 반복해서 풀이
# 만일 1-1-1-1-1-1-1이런식의 식이 주어진다면 상당히 비효율적일 수도?