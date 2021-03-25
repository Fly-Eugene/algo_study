#창용마을
import sys
sys.stdin = open('창용마을.txt', 'r')

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
    # search에서 다 방문하고 와!
    for i in range(1, N + 1):
        if visited[i] == 0:
            search(i)
            cnt += 1
    print('#{} {}'.format(t, cnt))



###################### for문으로 풀기
# import sys
# sys.stdin = open('창용마을.txt', 'r')
#
# T= int(input())
# for t in range(1,T+1):
#     N, M = map(int, input().split())
#     connect = [ [] for _ in range(M) ]
#     # connect = [ [], [], [], [], [] ]
#
#     a = [list(map(int, input().split())) for _ in range(M)]
#     # a = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]
#     # connect에 넣어 1, 2 다음에 2, 5가 오지
#     # 하나라도 갖고 있으면 입장시켜주고
#     # 하나도 없으면 다음 인덱스 리스트에 추가
#
#     for i in range(M):
#         idx = 0
#         for j in range(2):
#             if connect[i]:
#                 if connect[i][0] in connect[i-1]:
#                     connect[i].remove(connect[i][0])
#
#             if connect[idx] == [] or a[i][j] in connect[idx]:
#                 connect[idx] += a[i]
#             else:
#                 idx += 1
#
#
#
#     # for a in range(M-1):
#     #     for _ in range(2):
#     #         if connect[a+1]:
#     #             if connect[a+1][0] in connect[a]:
#     #                 connect[a+1].remove(connect[a+1][0])
#     print(connect)
#
#     # cnt = 0
#     # for x in range(len(connect)):
#     #     if connect[x]:
#     #         cnt += 1
#     #
#     # print('#{} {}'.format(t, cnt))