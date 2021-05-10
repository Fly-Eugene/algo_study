dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]


def where(ax, ay, bx, by):
    ach, bch, result = [], [], 0
    for a in range(A):
        if abs(bc[a][0] - ax) + abs(bc[a][1] - ay) <= bc[a][2]:
            ach.append((bc[a][3], a))
        else:
            ach.append((0, 0))
        if abs(bc[a][0] - bx) + abs(bc[a][1] - by) <= bc[a][2]:
            bch.append((bc[a][3], a))
        else:
            bch.append((0, 0))
    ach.sort(reverse=True)
    bch.sort(reverse=True)
    if ach[0] == bch[0]:
        result += ach[0][0]
        result += max(ach[1][0], bch[1][0])
    else:
        result += (ach[0][0] + bch[0][0])
    return result


for t in range(1, int(input())+1):
    M, A = map(int, input().split())
    move_a = [0] + list(map(int, input().split()))
    move_b = [0] + list(map(int, input().split()))
    ax, ay, bx, by = 1, 1, 10, 10
    bc = [list(map(int, input().split())) for a in range(A)]
    ans = 0
    for m in range(M+1):
        ax, ay = ax + dx[move_a[m]], ay + dy[move_a[m]]
        bx, by = bx + dx[move_b[m]], by + dy[move_b[m]]
        ans += where(ax, ay, bx, by)
    print('#{} {}'.format(t, ans))
