# 2806. N-Queen
import sys
sys.stdin = open('nqueen.txt', 'r')


# 공격 받는지,안받는지 체크
def check(i):
    for j in range(0, i):
        if rows[i] == rows[j] or abs(rows[i] - rows[j]) == i - j:
            return 0
    return 1


# 말을 어떻게 배치할까
def NQueen(r):
    if r == N:
        global cnt
        cnt += 1

    else:
        for j in range(N):
            rows[r] = j
            if check(r):
                NQueen(r + 1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    rows = [-1 for _ in range(N)]
    cnt = 0
    NQueen(0)

    print('#{} {}'.format(t, cnt))
