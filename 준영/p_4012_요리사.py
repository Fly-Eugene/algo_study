def sub_set(food):
    syn_sum = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            syn_sum += arr[food[i]][food[j]]
    return syn_sum


def p_set(idx, cnt=0):
    global min_dif
    if idx == N:
        return

    if cnt == N // 2:
        food1 = list()
        food2 = list()
        for i in range(N):
            if check[i]:
                food1.append(i)
                continue
            food2.append(i)
        dif = abs(sub_set(food1) - sub_set(food2))
        if dif < min_dif:
            min_dif = dif
        return

    check[idx] = 1
    p_set(idx + 1, cnt + 1)
    check[idx] = 0
    p_set(idx + 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 식재료 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min_dif = 20000
    for i in range(N):
        for j in range(i + 1, N):
            arr[i][j] = arr[i][j] + arr[j][i]
            arr[j][i] = arr[i][j]
    p_set(0)
    print('#{} {}'.format(tc, min_dif))