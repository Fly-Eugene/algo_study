import sys
sys.stdin = open('input.txt', 'r')

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def do_2048(start_r, start_c, d_index):
    q = list()
    r, c = start_r, start_c  # i 0
    for _ in range(N):
        if 0 <= r < N and 0 <= c < N and arr[r][c]:
            q.append(arr[r][c])
            arr[r][c] = 0
        r, c = r+dr[d_index], c+dc[d_index]
    print(q)
    # q.pop(0)으로 꺼내면서 넣어야됨
    while len(q):
        p = q.pop(0)
        if len(q) and p == q[0]:
            arr[start_r][start_c] = (p*2)
            q.pop(0)
        else:
            arr[start_r][start_c] = p
        start_r = start_r + dr[d_index]
        start_c = start_c + dc[d_index]


for tc in range(1, int(input())+1):
    N, di = input().split()
    N = int(N)
    print(N, di)

    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        print(arr[i])

    if di == 'up':
        for i in range(N):
            do_2048(0, i, 0)
    elif di == 'down':
        for i in range(N):
            do_2048(N-1, i, 1)
    # 여기서 망함. 시간부족
    elif di == 'left':
        for i in range(N):
            do_2048(i, 0, 2)
    elif di == 'right':
        for i in range(N):
            do_2048(i, N-1, 3)

    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, arr[i])))