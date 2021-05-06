dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, c_val, k, dis=1):
    global m_dis
    # 방문처리
    visit[r][c] = 1
    # 4방탐색
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        # 방문하지 않았다면
        if 0 <= nr < N and 0 <= nc < N and (visit[nr][nc] == 0):
            # 다음 위치가 현재높이보다 작다면
            if mountain[nr][nc] < c_val:
                dfs(nr, nc, mountain[nr][nc], k, dis+1)
            # 다음 위치가 현재높이보다 작지 않다면
            else:
                # k값이 존재한다면 산을 깎을 수 있음. 그리고 k로 깎은뒤 갈 수 있다면?
                if k and k >= (mountain[nr][nc] - c_val+1):
                    # 호출하고 k값을 0으로 만들어 더이상 깎을 횟수가 없다는 것을 알려주기
                    dfs(nr, nc, c_val-1, 0, dis+1)
    # 방문이 끝나면 다시 방문처리를 복구해준다.
    visit[r][c] = 0
    # 가장 많이 이동한 경우 갱신
    if dis > m_dis:
        m_dis = dis

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    # 원본배열
    mountain = [list(map(int, input().split())) for _ in range(N)]
    # 방문처리배열
    visit = [[0]*N for _ in range(N)]
    # 최대 이동거리, 가장 높은 봉우리
    m_dis, m_height = 1, 0
    # 최대 높이를 찾는다
    for i in range(N):
        m = max(mountain[i])
        m_height = m if m > m_height else m_height
    # 최대 높이일 경우 dfs를 돌린다.
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == m_height:
                dfs(r, c, mountain[r][c], K)
    print('#{} {}'.format(tc, m_dis))