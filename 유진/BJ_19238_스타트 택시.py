## 연료가 바닥나면 그 날의 업무가 끝남 (-1 반환)
## 현재 위치에서 가장 가까운 승객이 누구인지 찾기
## => 거리가 같다면, 행 번호가 작은 승객, 열 번호가 작은 승객을 태운다.
## 한 손님을 목적지로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료의 두 배가 충전됨


# 가장 가까이 있는 손님의 위치를 반환하는 함수
def client_bfs(taxi_r, taxi_c, dis, fuel):
    ## 매번 새로운 손님한테 가는 거리를 찾아야 하므로 update
    arr_copy = list(arr)

    queue = []
    queue.append([taxi_r, taxi_c, dis, fuel])

    dr = [1, -1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    while queue:
        # print(queue)
        r, c, dis, fuel = queue.pop(0)
        arr_copy[r][c] = 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                # 통로이고, 손님이 있는 위치가 아니면
                if arr_copy[nr][nc] == 0 and arr2[nr][nc] % 2 == 0:
                    n_fuel = fuel - 1
                    n_dis = dis + 1
                    queue.append([nr, nc, n_dis, n_fuel])
                # 손님들 위치를 표시한 arr2의 값이 홀수라면!! (손님들의 시작위치)
                elif arr2[nr][nc] % 2:
                    if dis > fuel:      # 가장 가까운 손님한테 가는데 연료가 부족하면,,
                        return -1
                    arr2[nr][nc] = 0    # 한 번 태운 손님은 다시 태우지 않도록 0으로 바꿈
                    n_fuel = fuel - 1
                    return nr, nc, n_fuel

## 손님의 위치에서 목적지까지 갈 수 있는지 확인하는 함수
def driving_bfs(nr, nc, dis, fuel):

    ## 목적지에 해당하는 값
    dst = arr2[nr][nc] + 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = []
    queue.append([nr, nc, dis, fuel])

    while queue:
        r, c, dis, fuel = queue.pop(0)
        arr_copy[r][c] = 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if arr_copy[nr][nc] == 0 and arr2[nr][nc] % 2 == 0:
                    n_dis = dis + 1
                    n_fuel = fuel - 1
                    queue.append([nr, nc, n_dis, n_fuel])
                elif arr2[nr][nc] == dst:
                    if fuel >= 0:
                        fuel -= 1
                        dis += 1
                        n_fuel = fuel + dis*2
                        print(fuel, dis)
                        return nr, nc, n_fuel   # 택시의 새로운 출발 지점, 그 때의 남은 연료
                    else: return -1


N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_copy = list(arr)
arr2 = [[0]*N for _ in range(N)]

# 행과 열번호는 1 이상 N 이하의 자연수
taxi_r, taxi_c = map(int, input().split())
taxi_r -= 1
taxi_c -= 1

for i in range(1, M*2, 2):
    st_r, st_c, end_r, end_c = map(int, input().split())
    arr2[st_r-1][st_c-1] = i
    arr2[end_r-1][end_c-1] = i+1

nr, nc, fuel = client_bfs(taxi_r, taxi_c, 0, fuel)
print(fuel)
print(driving_bfs(nr, nc, 0, fuel))

