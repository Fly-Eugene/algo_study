import heapq
import sys
input = sys.stdin.readline

def dijkstra(X):

    D[X] = 0
    q = []
    heapq.heappush(q, (0, X))

    while q:
        dist, now = heapq.heappop(q)
        if dist > D[now]:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

N, M, K, X = map(int, input().split())

## 인접 행렬 만들기
INF = int(1e9)
adj = [[] for _ in range(N+1)]

# 연결된 도시들의 가중치는 모두 1
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append((b, 1))

# 최소거리 기록하는 리스트 만들기
D = [INF]*(N+1)

dijkstra(X)

cnt = 0
for idx in range(1, N+1):
    if D[idx] == K:
        print(idx)
        cnt = 1

if cnt == 0:
    print(-1)
