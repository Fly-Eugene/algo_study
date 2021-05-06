# 백준 17070. 파이프
# 파이프 가로, 세로, 대각선
# 경로의 수

def dfs(x, y, pipe): # 좌표와 파이프
    global cnt
    if x == N-1 and y == N-1: # 도착 시
        cnt += 1
        return

    if pipe == 0 or pipe == 2: # 가로
        if y + 1 < N:
            if M[x][y+1] == 0:
                dfs(x, y+1, 0)

    if pipe == 1 or pipe == 2: # 세로
        if x + 1 < N:
            if M[x+1][y] == 0:
                dfs(x+1, y, 1)

    if pipe == 0 or pipe == 1 or pipe == 2: # 대각선
        if x + 1 < N and y + 1 < N:
            if M[x+1][y] == 0 and M[x][y+1] == 0 and M[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)

N = int(input())
M = [list(map(int, input().split())) for i in range(N)]
cnt = 0
dfs(0, 1, 0) # 시작파이프는 (0,1)
print(cnt)