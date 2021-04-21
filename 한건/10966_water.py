import sys
sys.stdin = open('10966_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    base = [[0]*M for i in range(N)]

    for i in range(N):
        line = input()
        for j in range(M):
            base[i][j] = line[j]
    # 여기까지 데이터 작업

    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    ans = 0
    for i in range(N):
        for j in range(M):
            if base[i][j] == 'L': # L 인곳에서는 BFS를 돈다
                queue = []
                queue.append([i, j])
                visited = [[0]*M for i in range(N)]
                visited[i][j] = 1 # 시작점 방문 체크
                while queue:
                    r, c = queue.pop(0)
                    if base[r][c] == 'W': # W가 pop 됐을 경우
                        ans += visited[r][c] - 1 # 값 조정을 위해서 -1 해줬으나 크게 신경 ㄴㄴ
                        break
                    for k in range(4): # 4방향 탐색 시작
                        dr = r + drow[k]
                        dc = c + dcol[k]
                        if -1 < dr < N and -1 < dc < M: # index 범위를 벗어나지 않고
                            if visited[dr][dc] == 0: # 방문하지 않았다면
                                queue.append([dr, dc])
                                visited[dr][dc] += visited[r][c] + 1
    print(f'#{test_case} {ans}')



