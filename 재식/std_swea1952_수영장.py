def s(m, cost):
    global res

    # 12를 오바했을때
    if m >= 13:
        if cost < res:
            res = cost

    # 1 ~ 12월
    else:
        s(m+1, cost + D * plan[m]) # 1일권
        s(m+1, cost + M1) # 1개월권
        s(m+3, cost + M3) # 3개월권

T = int(input())
for t in range(1, T+1):
    D, M1, M3, Y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    res = Y # 1년권과 비교

    s(1, 0) # 1월, 0원
    print("#{} {}".format(t, res))
