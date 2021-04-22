# # 위치별 최단거리 합 구하기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visit = [[- 1] * M for _ in range(N)]
    ans = 0
    q = []

    for i in range(N):
        road = input()
        for j in range(M):
            if road[j] == 'W':
                q.append((i, j))
                visit[i][j] = 0

    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] != - 1:
                    continue
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1

    for i in visit:
        ans += sum(i)
    print("#{} {}".format(t, ans))
