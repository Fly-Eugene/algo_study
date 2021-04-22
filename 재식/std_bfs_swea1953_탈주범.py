# 1953. 탈주범 검거
# 있을수 있는 장소 출력 = visit

pipe = { #사방, 상하, 좌우, 상우, 하우, 하좌, 상좌
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1)),
}

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # 맵길이, 범인위치, 탈출시간
    under = [list(map(int, input().split())) for _ in range(N)]

    visit = [[0]*M for _ in range(N)]
    visit[R][C], cnt = 1, 1 # 시작 위치와 카운트
    q = [(R, C)]

    while q:
        x, y = q.pop(0)

        for dx, dy in pipe[under[x][y]]: # 해당 파이프에서 갈수있는 방향으로 델타이동
            nx, ny = x+dx, y+dy

            if not (0 <= nx < N or 0 <= ny < M):
                continue

            if (-dx,-dy) in pipe[under[nx][ny]]: # 역방향 예외시키기
                if not (visit[nx][ny] and under[nx][ny]):
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                    if visit[nx][ny] <= L: # 탈출시간(L)보다 작거나 같을 때 cnt
                        cnt += 1

    print('#{} {}'.format(t, cnt))
