import sys
sys.stdin = open('파이프.txt', 'r')

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지 파이프의 한쪽끝을 (N, N)으로 이동

stack = [(0, 0), (0, 1)]
ans = 0
while stack:
    r2, c2 = stack.pop()
    r1, c1 = stack.pop()
    if r2 == N - 1 and c2 == N - 1:
        ans += 1
        continue
    # 가로, 세로, 대각선 검사
    if r1 == r2: # 가로로 놓여있다. 오른쪽으로만 밀 수 있다.
        if c2 + 1 < N and home[r2][c2+1] == 0: # 가로로 밈
            stack.append((r2, c2))
            stack.append((r2, c2+1))
        if r2 + 1 < N and c2 + 1 < N and not home[r2][c2+1] and not home[r2+1][c2] and not home[r2+1][c2+1]: # 45도 회전 밈
                stack.append((r2, c2))
                stack.append((r2+1, c2+1))
        continue
    if c1 == c2: # 세로로 놓여있다.
        if r2 + 1 < N and home[r2+1][c2] == 0: # 세로로 밈
            stack.append((r2, c2))
            stack.append((r2+1, c2))
            if c2 + 1 < N and not home[r2][c2+1] and not home[r2+1][c2] and not home[r2+1][c2+1]: # 45도
                stack.append((r2, c2))
                stack.append((r2+1, c2+1))
        continue
    if r1 != r2 and c1 != c2:
        if c2 + 1 < N and home[r2][c2+1] == 0: # ->
            stack.append((r2, c2))
            stack.append((r2, c2 + 1))
        if r2 + 1 < N and home[r2+1][c2] == 0: # 아래
            stack.append((r2, c2))
            stack.append((r2+1, c2))
        if r2 + 1 < N and c2 + 1 < N and not home[r2][c2+1] and not home[r2+1][c2] and not home[r2+1][c2+1]: # 대각
            stack.append((r2, c2))
            stack.append((r2+1, c2+1))
        continue

print(ans)
