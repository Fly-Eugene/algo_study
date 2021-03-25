def count_group(st):
    global cnt

    cnt += 1
    queue = []
    queue.append(st)

    while queue:
        r = queue.pop(0)
        if visited[r] == 0:
            visited[r] = 1
            for j in range(N+1):
                if arr[r][j] == 1:
                    queue.append(j)


    return

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    relation = []
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0

    # 서로 관계 표시하기
    for i in range(M):
        k, l = map(int, input().split())
        arr[k][l] = 1
        arr[l][k] = 1

    # visited 를 check하면서 그룹 개수 세기
    for i in range(1, N+1):
        if visited[i] == 1:
            pass
        else:
            count_group(i)

    # 혼자인 사람 찾기
    only_one = 0
    for i in range(1, N+1):
        if 1 not in arr[i]:
            only_one += 1

    res = cnt + only_one
    print(f'#{tc} {res}')
