def bfs(idx, dis):
    global max_idx
    global max_dis

    queue = []
    queue.append([idx, dis])
    visited[idx] = 1

    while queue:
        now, dis = queue.pop(0) # 현재 연락을 받은 번호 == now // 해당 번호가 몇 번째 연락을 받았는가 == dis

        for i in range(N):
            if adj[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                new_dis = dis + 1

                if max_dis < new_dis:   # 만약 현재 max_dis 보다 new_dis가 크면, max_idx 새롭게 갱신
                    max_idx = i
                    max_dis = new_dis      # max_dis도 갱신해줘야 하는거 잊지말기(기록)
                elif max_dis == new_dis:    # 만약 max_dis == new_dis이면 (max_idx, i)를 비교
                    if max_idx < i:
                        max_idx = i

                queue.append([i, new_dis])


for tc in range(1, 11):
    N, start = map(int, input().split())
    contact_list = list(map(int, input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)         # visitied를 사용해야 편하다!! (기록)

    # 서로 연결된 것을 adj(인접행렬)에 표시하기
    for i in range(0, N, 2):
        st, en = contact_list[i], contact_list[i+1]
        adj[st][en] = 1

    # for h in range(N+1):
    #     print(adj[h])

    max_dis = 0  # 가장 멀리간 연락
    max_idx = 0  # 멀리간 연락 중 어느 번호가 max인가

    # bfs 실행
    bfs(start, 0)

    print(f'#{tc} {max_idx}')

