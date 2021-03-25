import sys
sys.stdin = open('SWEA7465_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        lst[x][y] = 1

    stack = []
    starting_x, starting_y = 0, 0
    group = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dis = 0

            if lst[i][j] == 1 and visited[i][j] != 1:
                starting_x = i
                starting_y = j
                stack.append([starting_x, starting_y])
                visited[starting_x][starting_y] = 1

            while stack:
                a, b = stack.pop()
                if a == b:
                    dis += 1
                    continue
                for k in range(1, N + 1):
                    if lst[b][k] == 1 and visited[b][k] != 1:
                        stack.append([b, k])
                        visited[b][k] = 1
                        dis += 1

            if dis > 0:
                group += 1

    print(f'#{test_case} {group}')



