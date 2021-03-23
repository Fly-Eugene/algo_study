dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def move(row, col):
    global max_move
    q = list()
    q.append([row, col])
    m_val = 0  # 1일지도모름
    while len(q):
        size = len(q)
        for j in range(size):
            row, col = q.pop(0)
            for i in range(4):
                nr, nc = row+dr[i], col+dc[i]
                if 0 <= nr < N and 0 <= nc < N and (rooms[nr][nc] == (rooms[row][col]+1)):
                    q.append([nr, nc])
        m_val += 1
    return m_val


for tc in range(1, int(input())+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    start_n = N*N
    max_move = 0

    for r in range(N):
        for c in range(N):
            # 여기서 함수 호출
            num = move(r, c)
            start = rooms[r][c]
            if num == max_move and start < start_n:
                start_n = start
            if num > max_move:
                max_move = num
                start_n = start

    print('#{} {} {}'.format(tc, start_n, max_move))