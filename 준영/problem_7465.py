for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list() for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    visited = [0] * (N+1)
    company = 0
    for i in range(1, N+1):
        # 방문안했다면 방문처리하고 인접노드 확인
        if not visited[i]:
            company += 1
            visited[i] = 1
            s = []
            # 인접노드 확인해서 방문 안했다면 방문처리해주고 스택에 추가
            for item in arr[i]:
                if not visited[item]:
                    visited[item] = 1
                    s.append(item)
            # DFS로 더이상 탐색이 불가능해질때까지 방문하지 않은 노드를 조건탐색 후 스택에 추가
            while len(s):
                p = s.pop()
                for item in arr[p]:
                    if not visited[item]:
                        visited[item] = 1
                        s.append(item)
    print('#{} {}'.format(tc, company))