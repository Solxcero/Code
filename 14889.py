# 구현으로 분류되어 있는 문제입니다
# 주어지는 입력을 이중배열로 잘 받은 후에 위의 완전 탐색을 사용하여 풀어보세요
# 잘 안되면 파이썬 라이브러리의 itertools를 검색해보세요
import sys
from itertools import combinations, permutations

input = sys.stdin.readline
N = int(input()) # 인원
arr = [] #능력치 받기 

for n in range(N):
    arr.append(list(map(int,input().split())))
    
player = list(range(1,N+1))
case = list(combinations(player,N//2))
score_dif = []
for i,j in zip(case[:len(case)//2],list(reversed(case[len(case)//2:]))):
    team1 = list(permutations(i,2))
    team2 = list(permutations(j,2))
    score1, score2 = 0, 0
    for a,b in team1 :
        score1 += arr[a-1][b-1]
    for a,b in team2 :
        score2 += arr[a-1][b-1]
    dif = abs(score1-score2)
    score_dif.append(dif)
print(min(score_dif))