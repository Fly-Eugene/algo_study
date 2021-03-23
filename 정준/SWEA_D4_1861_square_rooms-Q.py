# 시작점이 r,c일 때 최대 값
def moverm(r, c):
    # UDLR
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = [(r, c)]
    max_cnt = 0
    while Q:
        ir, ic = Q.pop(0)
        val = rooms[ir][ic]
        for idx in range(4):
            nr, nc = ir + dr[idx], ic + dc[idx]
            if 0 <= nr < N and 0 <= nc < N:
                if rooms[nr][nc] == val + 1:
                    Q.append((nr, nc))
                    break
        max_cnt += 1
    return max_cnt


for t in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * (N*N+1)

    for i in range(N):
        for j in range(N):
            cnt[rooms[i][j]] = moverm(i, j)

    max_move = max(cnt)
    max_val = cnt.index(max_move)

    print('#{} {} {}'.format(t, max_val, max_move))
