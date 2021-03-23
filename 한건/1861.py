import sys
sys.stdin = open('1861_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [[0] * N for i in range(N)]

    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            lst[i][j] = line[j]

    # 시계방향
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    ans = 0
    sp = 0 #starting point

    for i in range(N):
        for j in range(N):
            stack = []
            length = 1
            stack.append((i, j))
            while stack:
                r, c = stack.pop(0)
                for k in range(4):
                    row = r + dr[k]
                    col = c + dc[k]
                    if -1 < row < N and -1 < col < N and lst[row][col] == lst[r][c] + 1:
                        stack.append((row, col))
                        length += 1
            if length > ans:
                ans = length
                sp = lst[i][j]
            elif length == ans:
                if lst[i][j] > sp:
                    continue
                else:
                    sp = lst[i][j]

    print(f'#{test_case} {sp} {ans}')


