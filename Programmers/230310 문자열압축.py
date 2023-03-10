def solution(s):
    count = 1001
    for i in range(1,len(s)):
        answer = ['']
        new_s = s
        while len(new_s) >= i:
            int_ = 1
            while new_s[:i] == answer[-1]:
                int_ += 1
                new_s = new_s[i:]
            else:
                if int_ > 1:
                    answer.insert(-1,str(int_))
                    answer.append(new_s[:i])
                    new_s = new_s[i:]
                else:
                    answer.append(new_s[:i])
                    new_s = new_s[i:]
        else:
            answer.append(new_s[:])
        
        
        if len(''.join(answer).strip()) < count:
            count = len(''.join(answer))

    if len(s) == 1:
        return 1
    else:
        return count
    
# 풀이 생각 : 압축을 위해 자른 것을 확인 후, 반복
# 반복문을 남발했는데 그렇지 않을 방법이?