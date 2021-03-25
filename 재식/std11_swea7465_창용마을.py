#창용마을
# import sys
# sys.stdin = open('창용마을.txt', 'r')

def search(idx):
    global visited
    # 방문했습니다.
    visited[idx] = 1

    # 방문한 곳에서 다음번으로 또 방문하기
    for i in link[idx]:
        if visited[i] == 0:
            search(i)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    link = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)
    # 인덱스마다 연결된 곳을 리스트화.
    # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

    cnt = 0
    visited = [0] * (N + 1)
    # 0번사람은 없으니까 1번부터 출발시키고
    # search에서 다 방문하고 와
    for i in range(1, N + 1):
        if visited[i] == 0:
            search(i)
            cnt += 1
    print('#{} {}'.format(t, cnt))
