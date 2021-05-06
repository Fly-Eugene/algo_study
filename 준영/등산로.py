dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, c_val, k, dis=1):
    global m_dis
    visit[r][c] = 1
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < N and (visit[nr][nc] == 0):
            if mountain[nr][nc] < c_val:
                dfs(nr, nc, mountain[nr][nc], k, dis+1)
            else:
                if k and k >= (mountain[nr][nc] - c_val+1):
                    dfs(nr, nc, c_val-1, 0, dis+1)
    visit[r][c] = 0
    if dis > m_dis:
        m_dis = dis

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    m_dis, m_height = 1, 0
    for i in range(N):
        m = max(mountain[i])
        m_height = m if m > m_height else m_height
            
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == m_height:
                dfs(r, c, mountain[r][c], K)
    print('#{} {}'.format(tc, m_dis))