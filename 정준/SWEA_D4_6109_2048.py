def rm_zero(lst):
    for i in range(N):
        for j in range(N):
            r, c = i, j
            if not lst[r][c]:
                if 0 <= i - dr[idx] < N and 0 <= j - dc[idx] < N:
                    lst[i][j], lst[i - dr[idx]][j - dc[idx]] = lst[i - dr[idx]][j - dc[idx]], lst[i][j]
    return lst


for t in range(1, int(input())+1):
    N, S = input().split()
    s = ['left', 'right', 'up', 'down']
    idx = s.index(S)
    N = int(N)
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    game = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if game[i][j]:
                if 0 <= i-dr[idx] < N and 0 <= j-dc[idx] < N:
                    if game[i][j] == game[i-dr[idx]][j-dc[idx]]:
                        game[i][j] *= 2
                        game[i-dr[idx]][j-dc[idx]] = 0
                    elif not game[i-dr[idx]][j-dc[idx]]:
                        game[i][j], game[i - dr[idx]][j - dc[idx]] = game[i - dr[idx]][j - dc[idx]], game[i][j]
    # 0 제거
    for _ in range(N):
        game = rm_zero(game)

    print('#{}'.format(t))
    for n in range(N):
        print(*game[n])