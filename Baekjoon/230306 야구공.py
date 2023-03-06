from itertools import permutations
import sys

def scoring(hitter_list):
    score = 0
    now_hitter = -1
    for scores in score_list:
      b_1, b_2, b_3, out_count = 0,0,0,0
      while out_count < 3:
          now_hitter = (now_hitter+1)%9
          if scores[hitter_list[now_hitter]] == 1:
              score += b_3
              b_1, b_2, b_3 = 1, b_1, b_2
          elif scores[hitter_list[now_hitter]] == 2:
              score += b_3+b_2
              b_1, b_2, b_3 = 0, 1, b_1
          elif scores[hitter_list[now_hitter]] == 3:
              score += b_3+b_2+b_1
              b_1, b_2, b_3 = 0, 0, 1
          elif scores[hitter_list[now_hitter]] == 4:
              score += 1+b_3+b_2+b_1
              b_1, b_2, b_3 = 0, 0, 0
          else:
              out_count += 1
    return score


# 이닝 수
inning = int(sys.stdin.readline())
# 이닝 당 점수 낼 것것
score_list = [list(map(int, sys.stdin.readline().split())) for i in range(inning)]
# 라인업
max_score = 0

for h in permutations(range(1,9),8):
  h = list(h)[:3] + [0] + list(h)[3:]
  score = scoring(h)
  if score > max_score:
        max_score = score

print(max_score)

# 풀이 생각 : 타자의 상태에 따라 아웃 혹은 진루하는 함수 + 모든 선수의 나열 경우의 수로 최대값 탐색
# permutation을 안쓰는 방법이 존재할까?
# 주루 상황과 아웃 카운트를 deque등으로 구현하면 시간적으로 더 이득인가 아닌가?