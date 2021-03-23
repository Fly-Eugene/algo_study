## 2차원 배열로 입력받는다
## 행 우선 순회
## 열 우선 순회로 각각 세로, 가로 오목을 판단한다.
## 대각선의 경우 2가지로 나눠서 진행한다.

import sys
sys.stdin = open('SWEA_11315.txt', 'r')


T = int(input())

for test in range(1, T+1):

    N = int(input())
    result = "NO"

    # NxN에 해당하는 2차원 배열을 입력받는다.
    arr = [list(map(str, input())) for _ in range(N)]


    # 행 우선 순회
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr[0])):
            if arr[i][j] == 'o':
                cnt += 1

                # 연속성이 5이면
                if cnt == 5:
                    result = "YES"
                    break
            else:
                # 연속성이 사라지면 cnt = 0
                cnt = 0


    # 열 우선 순회
    for j in range(len(arr[0])):
        cnt = 0
        for i in range(len(arr)):
            if arr[i][j] == 'o':
                cnt += 1

                if cnt == 5:
                    result = "YES"
                    break
            else:
                cnt = 0

    ## 대각선 우하향 (왼 => 중심)
    for i in range(0, N-4): # N-4는 연속성이 5가 될 가능성이 있는 라인을 설정하기 위함
        r = i
        c = 0
        cnt = 0
        while r < N:
            if arr[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    result = "YES"
                    break
            else:
                cnt = 0
            # 대각선 우측 아래로 한칸 옮기기
            r += 1
            c += 1

    ## 대각선 우하향 (중심 => 오른쪽)
    for i in range(0, N-4):
        r = 0
        c = i
        cnt = 0

        while c < N:
            if arr[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    result = "YES"
                    break
            else:
                cnt = 0

            # 우하향 대각선
            r += 1
            c += 1

    ## 대각선 좌하향(왼 => 중심)
    for i in range(N-1, 3, -1):
        r = 0
        c = i
        cnt = 0

        while c >= 0:
            if arr[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    result = "YES"
                    break
            else:
                cnt = 0

            # 좌하향 대각선
            r += 1
            c -= 1

    ## 좌하향 대각선(중심 => 오른쪽)
    for i in range(0, N-4):
        r = i
        c = N-1
        cnt = 0

        while r <= N-1:
            if arr[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    result = "YES"
                    break
            else:
                cnt = 0

            # 좌하향 대각선
            r += 1
            c -= 1

    print(f'#{test} {result}')