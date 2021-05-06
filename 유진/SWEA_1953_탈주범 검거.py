# up : 1,2,5,6
# down : 1,2,3,7
# left : 1,3,4,5
# right : 1,3,6,7

pipes = {'1':[0,1,2,3], '2':[0,1], '3':[2,3], '4':[0,3], '5':[1,3], '6':[1,2], '7':[0,2] }
go = {'0':'1256', '1':'1247', '2':'1345', '3':'1367'}

def bfs(r,c, dis):
    global L, res

    queue = []
    queue.append((r, c, dis))
    visited[r][c] = 1      # 맨홀 뚜껑 방문 체크
    res += 1

    while queue:
        r, c, dis = queue.pop(0)
        p = arr[r][c]  # 현재 위치의 파이프는?

        if dis >= L:   # 탈주범이 갈 수 있는 거리를 넘어서면
            return

        for i in pipes[p]:      # 원래 bfs는 4방 탐색이었다면, 현재는 pipe 별로 갈 수 있는 방향만 돈다.
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:     # 우선 인덱스를 체크해야 하고

                # 움직인 방향에 알맞은 pipe 모양이 있어야 움직일 수 있어!!
                if arr[nr][nc] in go[str(i)]:      # ex. go[0] : 1,2,5,6 파이프가 있어야 연결된 것임
                    if visited[nr][nc] == 0:    # 아직 체크되지 않은 곳이면
                        queue.append((nr, nc, dis+1))
                        res += 1
                        visited[nr][nc] = 1


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # N, M : 지도 크기 / R, C : 맨홀 위치 / L : 경과시간

    arr = [list(input().split()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    res = 0
    bfs(R, C, 1)    # 한시간 후 도착할 수 있는 곳이 맨홀 뿐임 ==> dis = 1로 시작

    # for i in range(N):
    #     print(visited[i])

    print(f'#{tc} {res}')
