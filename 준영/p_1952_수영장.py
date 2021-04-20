def p_set(idx, total):
    global min_fee
    if idx >= 12:
        min_fee = total if total < min_fee else min_fee
        return

    if months_3_table[idx] > months_3_fee:
        p_set(idx+3, total+months_3_fee)
    p_set(idx+1, total+pool_using[idx])



for tc in range(1, int(input())+1):
    day_fee, month_fee, months_3_fee, min_fee = map(int, input().split())
    pool_using = list(map(int, input().split()))
    for i in range(12):
        day = pool_using[i] * day_fee
        pool_using[i] = month_fee if day > month_fee else day
    months_3_table = [0] * 10 + [pool_using[-1]+pool_using[-2], pool_using[-1]]
    for i in range(10):
        months_3_table[i] = pool_using[i]+pool_using[i+1]+pool_using[i+2]
    p_set(0, 0)
    print('#{} {}'.format(tc, min_fee))