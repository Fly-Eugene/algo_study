# def dfs(r, c, idx, str):
#
#     if idx == 6:
#         check.add(str)
#         return
#
#     dr = [1, -1, 0, 0]  # 상하좌우
#     dc = [0, 0, -1, 1]
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0<= nr <4 and 0 <= nc <4:
#             dfs(nr, nc, idx+1, str+arr[nr][nc])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(input().split()) for _ in range(4)]
#
#     ## 🚩 set을 쓰는 이유에 대해서 기록하기
#     ## set. update & add의 차이점 기록하기
#     check = set()
#
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, 0, arr[i][j])
#
#     res = len(check)
#     print(f'#{tc} {res}')

def search(i, num):
    move = [-4, -1, 1, 4]
    if len(num) == 7:
        number.append(num)
        return

    num += str(grid[i])
    for idx in range(4):
        now = i + move[idx]
        if 0 <= now < 16:
            search(now, num)


for t in range(1, int(input()) + 1):
    grid = []
    for _ in range(4):
        grid += list(map(int, input().split()))

    num = ''
    number = []

    for k in range(16):
        search(k, num)

    number = set(number)

    print('#{} {}'.format(t, len(number)))







