## 처음에는 방문체크를 하면서 진행을 했다.
## 하지만 i,j로 반복문을 돌고 있는데 방문체크가 다시 reset 되지 않으면 문제가 발생한다.
## 또한 방문체크를 굳이 할 필요가 없다...?? 왔던 길을 되돌아가는 경우는 없으니까

def bfs(s_r, s_c, dis):
    max_dis = 0

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = []
    queue.append([s_r, s_c, dis])

    while queue:
        r, c, dis = queue.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            ## 인덱스 확인하기
            if 0 <= nr < N and 0 <= nc < N:
                if arr[r][c] + 1 == arr[nr][nc]:
                    n_dis = dis + 1
                    # 최대거리가 갱신됐는지 확인하기
                    if n_dis > max_dis:
                        max_dis = n_dis

                    queue.append([nr, nc, n_dis])

    return max_dis


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 정답이 될 좌표 & 최대 거리 저장 변수
    res_r, res_c = 0, 0
    max_res = 0

    for i in range(N):
        for j in range(N):
            d = bfs(i, j, 1)    # 현재 위치한 방의 개수도 세어야 하므로 처음 dis는 1

            ## 현재 최대거리와 같은 d가 return 됐을 때, 처음 시작점 크기 비교
            if max_res == d:
                if arr[res_r][res_c] > arr[i][j]:
                    res_r, res_c = i, j

            ## d가 더 크다면 무조건 처음 시작점 바꾸기
            elif max_res < d:
                max_res = d
                res_r, res_c = i, j

    print(f'#{tc} {arr[res_r][res_c]} {max_res}')

