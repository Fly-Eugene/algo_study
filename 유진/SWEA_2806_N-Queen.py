
## 백트래킹...?
def n_queen(r, c):
    # print('n_queen', r, c)
    global cnt
    global visited

    no = [0] * (N+1)       # 다음행이 대각선 규칙으로 올 수 없는 곳을 표시
    if r == 1:
        visited = [0 for _ in range(N+1)]

    visited[c] = r

    if r == N:
        # print('완성!!')
        cnt += 1
        return

    # 다음행에 위치할 수 없는 곳을 no에 표시하기
    for i in range(1, N+1):
        if visited[i] != 0:
            diff_r = (r+1) - visited[i]

            if 0 < i - diff_r <= N:
                no[i-diff_r] = 1
            if 0 < i + diff_r <= N:
                no[i+diff_r] = 1

    # print('visited', visited)
    # print('no', no)

    for i in range(1, N+1):
        if no[i] == 0 and visited[i] == 0:
            n_queen(r+1, i)

            # 원상복구가 필요해..?
            visited[i] = 0

    visited[c] = 0
    return


#####
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    stack = []
    cnt = 0

    for nc in range(1, N+1):
        n_queen(1, nc)

    print(f'#{tc} {cnt}')

