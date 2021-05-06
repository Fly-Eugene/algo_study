# 최대상금

T = int(input())
for t in range(1, T+1):
    reward, change = input().split()
    change = int(change)
    N = len(reward)

    # ans이 tmp가 되므로 add하기 위해 set()
    ans = set([reward])
    tmp = set()

    # 교환 횟수만큼
    for n in range(change):

        while ans:
            # split
            s = ans.pop()
            s = list(s)

            # N = len(reward)
            for i in range(N):
                for j in range(i+1, N):
                    s[i], s[j] = s[j], s[i]
                    tmp.add(''.join(s))
                    # 바꾼거 돌려놓기
                    s[i], s[j] = s[j], s[i]
        # 32888
        ans, tmp = tmp, ans

    print('#{} {}'.format(t, max(map(int, ans))))