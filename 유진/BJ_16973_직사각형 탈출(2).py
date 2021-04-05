
def box_dfs(sr, sc, dis):
    queue = []
    queue.append([sr, sc, dis])
    visited[sr][sc] = 1

    while queue:
        sr, sc, dis = queue.pop(0)

        if sr == fr and sc == fc:
            return dis

        # 상
        stop = 0
        if sr-1 >= 0 and visited[sr-1][sc] == 0:    # 인덱스와 방문체크

            for j in range(sc, sc+W):
                if arr[sr-1][j] == 1:
                    stop = 1
                    break
            if stop == 0:
                n_sr, n_sc, n_dis = sr-1, sc, dis+1
                queue.append([n_sr, n_sc, n_dis])   # queue에 append
                visited[n_sr][n_sc] = 1             # 방문체크 해야즤

        # 하
        stop = 0
        if sr+H < N and visited[sr+1][sc] == 0:   # 인덱스 & 방문체크
            for j in range(sc, sc+W):
                if arr[sr+H][j] == 1:
                    stop = 1
                    break
            if stop == 0:
                n_sr, n_sc, n_dis = sr+1, sc, dis+1
                queue.append([n_sr, n_sc, n_dis])
                visited[n_sr][n_sc] = 1

        # 좌
        stop = 0
        if sc-1 >= 0 and visited[sr][sc-1] == 0:
            for i in range(sr, sr+H):
                if arr[i][sc-1] == 1:
                    stop = 1
                    break
            if stop == 0:
                n_sr, n_sc, n_dis = sr, sc-1, dis+1
                queue.append([n_sr, n_sc, n_dis])
                visited[n_sr][n_sc] = 1

        # 우
        stop = 0
        if sc+W < M and visited[sr][sc+1] == 0:
            for i in range(sr, sr+H):
                if arr[i][sc+W] == 1:
                    stop = 1
                    break
            if stop == 0:
                n_sr, n_sc, n_dis = sr, sc+1, dis+1
                queue.append([n_sr, n_sc, n_dis])
                visited[n_sr][n_sc] = 1

    # queue를 다 돌았는데 목적지에 도착하지 못했다면
    return -1
###############################################################################

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

H, W, sr, sc, fr, fc = map(int, input().split())
sr, sc = sr-1, sc-1
fr, fc = fr-1, fc-1

ans = box_dfs(sr, sc, 0)
print(ans)

