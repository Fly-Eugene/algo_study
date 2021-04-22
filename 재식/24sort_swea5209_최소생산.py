def C(j, cost):
    global res

    if j == N:
        if res > cost:
            res = cost
        return

    if res < cost:
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            C(j+1, cost + board[j][i])
            visit[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    res = 9999999

    C(0, 0)
    print('#{} {}'.format(t, res))