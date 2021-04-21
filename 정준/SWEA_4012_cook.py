def perm(idx, ele):
    # ele는 선택한 원소의 갯수
    if ele == N//2:
        a, b, A, B = [], [], 0, 0
        for i in range(N):
            if sel[i]:
                a.append(i)
            else:
                b.append(i)
        for i in range(N//2):
            for j in range(N//2):
                A += food[a[i]][a[j]]
        for i in range(N // 2):
            for j in range(N // 2):
                B += food[b[i]][b[j]]
        gap = abs(A-B)
        global deli_gap
        deli_gap = gap if gap < deli_gap else deli_gap
        return
    elif idx >= N:
        return
    sel[idx] = 1
    perm(idx+1, ele+1)
    sel[idx] = 0
    perm(idx + 1, ele)


for t in range(1, int(input()) + 1):
    N = int(input())
    sel = [0] * N
    food = [list(map(int, input().split())) for _ in range(N)]
    deli_gap = 999999
    perm(0, 0)
    print(f'#{t} {deli_gap}')
