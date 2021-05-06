def check_v(r, c): # 세로
    if r+1 >= N or arr[r+1][c]: return False
    return True

def check_h(r, c): # 가로
    if c+1 >= N or arr[r][c+1]: return False
    return True

def check_dia(r, c): # 대각
    if r+1 >= N or c+1 >= N or arr[r+1][c] or arr[r][c+1] or arr[r+1][c+1]:
        return False
    return True

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

# r, c, 파이프상태
stack = [(0, 1, 2)]  # 세번째 인수가 현재 파이프 상태를 나타낸다.
while stack:
    r, c, condition = stack.pop()

    if r == N-1 and c == N-1:
        cnt += 1
        continue

    if condition == 2:  # 가로 상태일 때
        if check_h(r, c): stack.append((r, c+1, 2))

    elif condition == 3:  # 세로 상태일 때
        if check_v(r, c): stack.append((r+1, c, 3))

    else:  # 대각 상태일 때
        if check_h(r, c): stack.append((r, c+1, 2))
        if check_v(r, c): stack.append((r+1, c, 3))
    # 대각선은 모든 방향에서 가능하므로
    if check_dia(r, c): stack.append((r+1, c+1, 4))

print(cnt)