
def dfs(chg):
    global res
    ## 바꾼 횟수 끝남
    if chg == 0:
        if res < int(''.join(num_list)):    # join 사용법 기록하기
            res = int(''.join(num_list))
        return
    # 바꾼 횟수 덜 끝남
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            # 두 자리를 바꿔준다.
            num_list[i], num_list[j] = num_list[j], num_list[i]
            n_chg = chg - 1

            # 현재 바꾼 횟수 & 리스트 숫자의 순서가 set에 있다면?
            # 이미 다음 경우의 수도 고려했었다는 의미
            if (n_chg, int(''.join(num_list))) not in num_set:
                num_set.add((n_chg, int(''.join(num_list))))  # 아직 고려하지 않았으므로 set에 추가
                dfs(n_chg)

            # dfs 를 벗어나면 원상 복구 해주기
            num_list[i], num_list[j] = num_list[j], num_list[i]

T = int(input())

for tc in range(1, T+1):
    num, chg = input().split()
    chg = int(chg)
    num_list = [i for i in num]
    res = 0
    num_set = set()

    dfs(chg)

    print(f'#{tc} {res}')

