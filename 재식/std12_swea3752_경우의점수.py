import sys
sys.stdin = open('시험점수.txt','r')

# 점수가 나올 수 있는 경우의 수
# 2, 3, 5 => 0, 2, 3, 5, 7, 8, 10

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    score = {0}
    for i in nums: # [2, 3, 5]
        for j in list(score): # [0]
            score.add(i+j)

    res = len(score)
    print("#{} {}".format(t, res))