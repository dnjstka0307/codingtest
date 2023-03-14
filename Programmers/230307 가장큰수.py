def solution(numbers):
    new = [[int((str(i)*4)[:4]), len(str(i))] for i in numbers]
    new = sorted(new, reverse=True)
    ans = ''
    for i in new:
        ans += str(i[0])[:i[1]]
    ans = str(int(ans))
    return ans
    
# 풀이 생각 : list 최대 크기가 100,000이기에 반복문 중첩 or permutation시 문제 발생 생각, 다른 방식으로 풀이 필요
# 과거 고등수학 문제 중에 이와 비슷하게 풀었던 경우 ~ 갖고 있는 수로 최대n자리의 수를 만들고 싶다면, n자리까지 갖고 있는 수를 반복한뒤 크기 비교

# 수학적인 테크닉 외에 정렬알고리즘을 사용해서 풀이 방법이 있을까?