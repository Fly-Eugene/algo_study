dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, dis):
    global max_dis
    stack = []
    stack.append((r, c, dis))

    while stack:
        r, c, dis = stack.pop()   # 맨 뒤에걸 뽑음

        for i in range(4):  # 4방 탐색
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N:   # 인덱스 검사
                if is_map[nr][nc] < is_map[r][c]:    # 현재 위치의 높이보다 낮아야 됨
                    stack.append((nr, nc, dis+1))
                    if max_dis < dis+1:
                        max_dis = dis+1

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    is_map = [list(map(int, input().split())) for _ in range(N)]

    # 최대 높은 위치 찾기
    high = 0
    for i in range(N):
        if high < max(is_map[i]):
            high = max(is_map[i])

    high_list = []
    for r in range(N):
        for c in range(N):
            if is_map[r][c] == high:
                high_list.append((r, c))     # 최대높이 지점 high_list에 append 하기


    # 위치 하나씩 돌면서 깎아보기,,? 이게 맞는걸까요오오~
    max_dis = 0
    for r in range(N):
        for c in range(N):
            # if (r, c) in high_list:
            #     continue

            for k in range(1, K+1):
                is_map[r][c] -= k
                # print('현재 위치는', r, c, '얼마나 깎을건데', k, is_map[r][c])
                for h in range(len(high_list)):
                    dfs(high_list[h][0], high_list[h][1], 1)

                # print('현재 최고 길이는', max_dis)
                is_map[r][c] += k   # 산 한번 깎고 원상복귀 시켜주기

    print(f'#{tc} {max_dis}')









