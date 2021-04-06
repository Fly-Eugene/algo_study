def BFS(sr, sc, visited, fr, fc):
    Q = [(sr, sc)]
    visited[sr][sc] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c = Q.pop(0)
        if r == fr and c == fc:
            break
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return visited[fr][fc] - 1


N, M = map(int, input().split())
rec = [list(map(int, input().split())) for _ in range(N)]
H, W, sr, sc, fr, fc = map(int, input().split())
H, W, sr, sc, fr, fc = H - 1, W - 1, sr - 1, sc - 1, fr - 1, fc - 1
visited = [[0] * M for _ in range(N)]

# 사각형의 시작점이 위치할수 없는 부분 미리 방문 표시
# 벽부분
for i in range(N):
    for j in range(M):
        if rec[i][j] == 1:
            for ix in range(i, i - H - 1, -1):
                for jx in range(j, j - W - 1, -1):
                    visited[ix][jx] = 1
# 테두리 부분
for i in range(N - 1, N - 1 - H, -1):
    visited[i] = [1] * M
for i in range(N - H):
    for j in range(M - 1, M - 1 - W, -1):
        visited[i][j] = 1

if visited[fr][fc] == 1:
    print(-1)
else:
    print(BFS(sr, sc, visited, fr, fc))
