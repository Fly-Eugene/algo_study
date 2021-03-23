for t in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # UDLR
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = [0] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            val = rooms[i][j]
            for idx in range(4):
                r, c = i + dr[idx], j + dc[idx]
                if 0 <= r < N and 0 <= c < N and rooms[r][c] == val+1:
                    cnt[rooms[i][j]] = 1
                    break

    for i in range(N*N, 0, -1):
        # 인접한곳이 있다는 뜻이므로
        if cnt[i]:
            cnt[i] = cnt[i+1]+1
        # 자기 자신을 방문
        else:
            cnt[i] = 1

    max_move = max(cnt)
    idx = cnt.index(max_move)
    print('#{} {} {}'.format(t, idx, max_move))
