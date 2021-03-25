def powerset(idx):
    tot_scores = 0
    global N, result
    if idx == N:
        for i in range(N):
            if sel[i] == 1:
                tot_scores += scores[i]
            else:
                tot_scores += 0

        if tot_scores not in result:
            result.append(tot_scores)
        return
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 문제의 수
    scores = list(map(int,input().split()))
    sel = [0] * N
    result = []

    powerset(0)

    print(f'#{tc} {len(result)}')

# 백트래킹 요소가 필요하다..!


