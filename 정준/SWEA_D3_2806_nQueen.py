def check(x, y, lst):
    for i in range(len(lst)):
        # 가로 , 대각선 체크
        if lst[i][1] == y or abs(lst[i][0]-x) == abs(lst[i][1]-y):
            return False
    return True


def nQueen(x, y, queen):
    global ans
    queen.append((x, y))
    if len(queen) == N:
        ans += 1
    x += 1
    for i in range(N):
        if check(x, i, queen):
            nQueen(x, i, queen)
            queen.pop()


for t in range(1, int(input()) + 1):
    N = int(input())
    ans = 0
    for i in range(N):
        queen = []
        nQueen(0, i, queen)
    print('#{} {}'.format(t, ans))
