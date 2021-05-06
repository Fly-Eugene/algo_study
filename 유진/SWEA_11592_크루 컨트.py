
T = int(input())

for tc in range(1, T+1):
    D, N = map(int, input().split())
    max_time = 0
    max_st, max_v = 0, 0
    for _ in range(N):
        st, v = map(int, input().split())
        time = (D-st) / v

        if time > max_time:
            max_time = time
            max_st, max_v = st, v

    res = (D*max_v) / (D-max_st)

    print(f'#{tc} {res}')
