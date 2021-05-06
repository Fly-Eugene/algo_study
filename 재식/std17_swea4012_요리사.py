# 4012. 음식 조합찾기
# 행렬표 음식에서 대칭 점수 합에서 최소차

def dfs(idx, k):
    global res
    if idx == N // 2:

        A = []  # 재료리스트
        B = []
        for j in range(N):
            if visit[j]: # 방문여부에 따라 담기
                A.append(j)
            else:
                B.append(j)

        score_A = dish(A) # dish의 점수를 여기로
        score_B = dish(B)
        if abs(score_A - score_B) < res:
            res = abs(score_A - score_B)
        return

    for i in range(k, N):
        if not visit[i]:
            visit[i] = 1
            dfs(idx + 1, i + 1)
            visit[i] = 0

def dish(C): # 점수 조합
    score = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            score += food[C[i]][C[j]] + food[C[j]][C[i]]
    return score


T = int(input())
for t in range(1, T+1):
    N = int(input())
    visit = [0 for _ in range(N)]
    food = [list(map(int, input().split())) for _ in range(N)]
    res = 99999

    dfs(0, 0)
    print('#{} {}'.format(t, res))
