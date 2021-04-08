dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global front, rear
    res = 0
    while rear != front:
        r, c = q[front]
        front += 1
        res += visit[r][c]
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc] == -1:
                    q.append((nr, nc))
                    rear += 1
                    visit[nr][nc] = visit[r][c]+1
    return res

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    visit = [[-1]*M for _ in range(N)]
    q = list()
    front, rear = 0, 0
    for r in range(N):
        line = input()
        for c in range(M):
            if line[c] == 'W':
                q.append((r, c))
                rear += 1
                visit[r][c] = 0
    print('#{} {}'.format(tc, bfs()))