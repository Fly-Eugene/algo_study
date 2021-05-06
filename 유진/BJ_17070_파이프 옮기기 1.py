import sys

move = {1: [(0, 1, 1), (1, 1, 3)],
        2: [(1, 0, 2), (1, 1, 3)],
        3: [(0, 1, 1), (1, 0, 2), (1, 1, 3)]}       # (nr, nc, pipe)

def pipe_dfs(r, c, pipe):
    global cnt, arr

    if r == N-1 and c == N-1:
        cnt += 1
        return

    if pipe == 1:
        if 0 <= r < N and 0 <= c+1 < N:
            if arr[r][c+1] == 0:
                pipe_dfs(r, c+1, 1)
        if 0 <= r+1 < N and 0 <= c+1 < N:
            if arr[r+1][c+1] == 0 and arr[r][c+1] == 0 and arr[r+1][c] == 0:
                pipe_dfs(r+1, c+1, 3)
    elif pipe == 2:
        if 0 <= r+1 < N and 0 <= c < N:
            if arr[r+1][c] == 0:
                pipe_dfs(r+1, c, 2)
        if 0 <= r+1 < N and 0 <= c+1 < N:
            if arr[r+1][c+1] == 0 and arr[r][c+1] == 0 and arr[r+1][c] == 0:
                pipe_dfs(r+1, c+1, 3)
    elif pipe == 3:
        if 0 <= r < N and 0 <= c+1 < N:
            if arr[r][c+1] == 0:
                pipe_dfs(r, c+1, 1)
        if 0 <= r+1 < N and 0 <= c < N:
            if arr[r+1][c] == 0:
                pipe_dfs(r+1, c, 2)
        if 0 <= r+1 < N and 0 <= c+1 < N:
            if arr[r+1][c+1] == 0 and arr[r][c+1] == 0 and arr[r+1][c] == 0:
                pipe_dfs(r+1, c+1, 3)


input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
pipe_dfs(0, 1, 1)
print(cnt)
