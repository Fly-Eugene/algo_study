for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    already = [0] * N
    group = 0

    for _ in range(M):
        a, b = map(int, input().split())
        # 둘다 무리 없으면
        if not already[a-1] and not already[b-1]:
            group += 1
            already[a-1], already[b-1] = group, group
        # 둘중하나가 무리 없으면
        elif already[a-1] and not already[b-1]:
            already[b-1] = already[a-1]
        elif not already[a-1] and already[b-1]:
            already[a-1] = already[b-1]
        # 둘다 이미 소속된 무리가 있다면
        else:
            val = already[b-1]
            for i in range(N):
                if already[i] == val:
                    already[i] = already[a-1]
    # 아직도 무리 없는 사람은 혼자가 한무리
    ans = already.count(0)
    already = list(set(already))
    ans = ans + len(already) - 1 if 0 in already else ans + len(already)

    print('#{} {}'.format(t, ans))
