import sys
input = sys.stdin.readline

num = int(input())
preds = []
for _ in range(num):
    pred = int(input())
    preds.append(pred)

preds.sort()
ans = sum(list(map(lambda x : abs(x[0]+1-x[1]), enumerate(preds))))
print(ans)

# 풀이 생각 : 최소값이 되기위해서는 예상등수를 그냥 sort해서 차례대로 지정해주면 최소값이 된다
# 시간 초과 이슈(아마 sort에서 난듯)를 백준의 무적인 sys입력을 사용해서 해결했는데 메서드sort가 아닌 다른 시간복잡도가 더 개선되는 커스텀 sort함수를 만들어서
# 사용한다면 sys를 굳이 사용하지 않아도 되어서 좋을듯하다