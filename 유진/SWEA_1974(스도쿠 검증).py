
## 풀이방법
# 1. mini_box 에서 겹치지 않는지 확인
# 2. 가로로 겹치지 않는지 확인
# 3. 세로로 겹치지 않는지 확인

import sys
sys.stdin = open('SWEA_1974.txt', 'r')


def mini_box(arr, nr, nc):
    dr = [1, -1, 0, 0, -1, -1, 1, 1]    # 상하좌우 대각선 4방향
    dc = [0, 0, -1, 1, -1, 1, 1, -1]

    check = [0] * 10      # 1~9까지 하나씩 들어있는지 확인하기 위한 리스트 (카운팅 정렬 앞단계)
    check[arr[nr][nc]] += 1  # 현재 값을 인덱스로 활용해 카운트

    for i in range(len(dr)):
        r = nr + dr[i]
        c = nc + dc[i]

        check[arr[r][c]] += 1
        if check[arr[r][c]] > 1:
            return False
    return True


T = int(input())

for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    row = True
    col = True
    box = True
    res = 0

    # 가로로 겹치는지 check
    for i in range(N):
        check = [0] * (N+1)    # 0이 포함되진 않지만, 인덱스로 처리하므로 인덱스9 까지인 10개를 만들어야함
        for j in range(N):
            check[arr[i][j]] += 1
            if check[arr[i][j]] > 1:
                row = False

    # 세로로 겹치는지 check
    for j in range(N):
        check = [0] * (N+1)
        for i in range(N):
            check[arr[i][j]] += 1
            if check[arr[i][j]] > 1:
                col = False

    # mini_box에서 겹치는지 check
    for nr in range(1, 10, 3):
        for nc in range(1, 10, 3):
            if mini_box(arr, nr, nc) == False:
                box = False

    # 겹치는게 하나도 없다면 res = 1
    if row:
        if col:
            if box:
                res = 1

    print(f'#{tc} {res}')









