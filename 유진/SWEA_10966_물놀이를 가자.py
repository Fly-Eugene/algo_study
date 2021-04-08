from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    queue = deque()
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                queue.append((r, c))  # 튜플로 바꿔봄...
                visited[r][c] = 0     # 물이 발견된 곳이니까 거리를 0으로 둔다.

    res = 0
    while queue:
        wr, wc = queue.popleft()
        # print(wr, wc, dis)
        for i in range(4):
            nr, nc = wr + dr[i], wc + dc[i]

            if 0 <= nr < N and 0 <= nc < M:  # 인덱스 검사
                if visited[nr][nc] == -1:  # 방문 검사

                    queue.append((nr, nc))  # 무조건 queue.append
                    visited[nr][nc] = visited[wr][wc] + 1  # 현재 거리가 이만큼
                    res += visited[nr][nc]

    print(f'#{tc} {res}')
