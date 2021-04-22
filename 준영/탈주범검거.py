dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

pipe = {
    -1: [], 0: [],
    1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3], 4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2],
}

T = int(input())
for tc in range(1, T + 1):
    # 세로크기, 가로크기, 멘홀세로, 멘홀가로, 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    q = list()
    q.append((R, C))
    while q:
        # print(L, "바퀴 남았습니다")
        size = len(q)
        for _ in range(size):
            r, c = q.pop(0)
            for i in pipe[road[r][c]]:
                nr, nc = r+dr[i], c+dc[i]
                # 지도안에 위치하는지
                if 0 <= nr < N and 0 <= nc < M:
                    togo = i
                    if i % 2: # 홀수면
                        togo -= 1
                    else: # 짝수면
                        togo += 1
                    # 되돌아 갈 수 있다면 연결 된 것
                    if togo in pipe[road[nr][nc]]:
                        q.append((nr, nc))
            if road[r][c] > 0:
                cnt += 1
            road[r][c] = -1
        L -= 1
        if L == 0:
            break
    print('#{} {}'.format(tc, cnt))
