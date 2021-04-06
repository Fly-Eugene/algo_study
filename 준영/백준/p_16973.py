def BFS(Sr, Sc, Fr, Fc):
    q = list()
    q.append([Sr, Sc, 0])
    visit[Sr][Sc] = 1
    while q:
        Sr, Sc, dis = q.pop(0)

        # pop위치가 목적지와 같은지 확인
        if Sr == Fr and Sc == Fc:
            return dis

        if Sr-1 >= 0 and not visit[Sr-1][Sc]: # 상이 범위 내에 있고, 방문하지 않았다면
            for c in range(Sc, Sc+W):
                if plate[Sr-1][c]: break
            else:
                q.append([Sr-1, Sc, dis+1])
                visit[Sr-1][Sc] = 1

        if Sr+H < N and not visit[Sr+1][Sc]: # 하가 범위 내에 있고, 방문하지 않았다면
            for c in range(Sc, Sc+W):
                if plate[Sr+H][c]: break
            else:
                q.append([Sr+1, Sc, dis+1])
                visit[Sr+1][Sc] = 1

        if Sc-1 >= 0 and not visit[Sr][Sc-1]: # 좌가 범위 내에 있고, 방문하지 않았다면
            for r in range(Sr, Sr+H):
                if plate[r][Sc-1]: break
            else:
                q.append([Sr, Sc-1, dis+1])
                visit[Sr][Sc-1] = 1

        if Sc+W < M and not visit[Sr][Sc+1]: # 우가 범위 내에 있고, 방문하지 않았다면
            for r in range(Sr, Sr+H):
                if plate[r][Sc+W]: break
            else:
                q.append([Sr, Sc+1, dis+1])
                visit[Sr][Sc + 1] = 1
    return -1

N, M = map(int, input().split())
plate = [list(map(int, input().split()))for _ in range(N)]
visit = [[0] * M for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
Sr, Sc, Fr, Fc = Sr-1, Sc-1, Fr-1, Fc-1
cnt = BFS(Sr, Sc, Fr, Fc)
print(cnt)