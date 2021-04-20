# 1일: 10원/ 1달: 40원/ 3달: 100원/ 1년:300원
def swim(m, money):
    global min_money

    if m >= 12:     # 인덱스 상으로 plan[11]이 12월임
        if money < min_money:
            min_money = money

    else:
        # 1일권 구입
        swim(m+1, money+plan[m]*day)
        # 1달권 구입
        swim(m+1, money+month)
        # 3달권 구입
        swim(m+3, money+tt_month)


T = int(input())

for tc in range(1, T+1):
    day, month, tt_month, year = map(int, input().split())
    plan = list(map(int, input().split()))

    min_money = year
    swim(0, 0)
    print(f'#{tc} {min_money}')
