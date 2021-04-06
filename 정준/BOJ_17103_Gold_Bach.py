# 에라토네스의 체
MAX = 1000000
check = [True] * (MAX+1)
prime_lst = []
check[0], check[1] = False, False

for i in range(2, MAX+1):
    if check[i]:
        prime_lst.append(i)
        for j in range(2*i, MAX+1, i):
            check[j] = False

for t in range(int(input())):

    N = int(input())
    n = N//2
    cnt = 0
    idx = 0
    # 소수인지 비교
    while prime_lst[idx] <= n:
        now = N - prime_lst[idx]
        if check[now]:
            cnt += 1
        idx += 1
    print(cnt)



