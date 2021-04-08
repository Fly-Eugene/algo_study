# 1. 언니의 가벽 처리를 rec으로 바꿔줘야함
# 2. 16번째 줄 즈음에 움직일 곳의 rec 검사를 한 번 더 해줘야함 (갈 수 있는 곳인지)
# 3. 15반째 줄 즈음에 visited check는 그대로 유지한다. (방문을 했던 곳인지 체크)
def BFS(sr, sc, visited, fr, fc):
    Q = [(sr, sc)]
    rec[sr][sc] = 1
    # direction = ['위', '아래', '왼쪽', '오른쪽']
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                Q.append((nr, nc))
                rec[nr][nc] = rec[r][c] + 1
                if nr == fr and nc == fc:
                    break
                # print(direction[i], end=', ')
    return rec[fr][fc] - 1


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

for _ in range(N):
    print(visited[_])
print(BFS(sr, sc, visited, fr, fc))