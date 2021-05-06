def n_queen(idx, stack):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        for r, c in stack: # 스택에서 r, c 꺼내서 겹치는지 확인
            if c == i or (abs(r-idx) == abs(c-i)): # 겹치는 자리가 있으면
                break
        else: # 겹치는 애가 없으면
            n_queen(idx+1, stack+[(idx, i)])

for tc in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    for i in range(N):
        n_queen(1, [(0, i)])
    print('#{} {}'.format(tc, cnt))