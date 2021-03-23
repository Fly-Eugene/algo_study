T = int(input())
for tc in range(1, T+1):
    N, B = list(map(int, input().split()))
    H = list(map(int, input().split()))
    total = 0
    # 부분집합 풀기..
    sel = [0] * N
    idx = 0
    result = []

    def perm(idx):
        if idx == N: # 원소의 선택 여부를 모두 마쳤다면..
            tmp = []
            for i in range(N):
                if sel[i]:
                    tmp.append(H[i])
            if sum(tmp) >= B:
                result.append(sum(tmp))
            return
        else:
            sel[idx] = 1
            perm(idx+1)
            sel[idx] = 0
            perm(idx+1)
    perm(0)

    # 위의 코드에 합쳐서 할 수 있을 거 같다...
    min = 999999
    # B보다 크거나 같은 키 조합(result) 중에서 최솟값 찾기
    for num in result:
        if min >= num:
            min = num
    print(f'#{tc} {min - B}')
