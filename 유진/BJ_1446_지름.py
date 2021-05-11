import sys
import heapq
input = sys.stdin.readline

def dijkstra(st):
    distance[st] = 0
    queue = []
    heapq.heappush(queue, (st, 0))

    while queue:
        now, dis = heapq.heappop(queue)
        if distance[now] < dis:
            continue
        for i in adj_list[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))

    return distance[D]

N, D = map(int, input().split())
adj_list = [[] for i in range(D+1)]

for _ in range(N):
    start, end, dis = map(int, input().split())
    if end > D:
        continue
    adj_list[start].append((end, dis))

# 각 위치는 +1 위치만큼 가는거리가 1이다.
for i in range(D):
    adj_list[i].append((i+1, 1))

INF = 10000
distance = [INF]*(D+1)

print(dijkstra(0))