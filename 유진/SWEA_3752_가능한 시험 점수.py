T = int(input())

for tc in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    point_sum = [0]

    visited = [0] * (sum(point) + 1)
    visited[0] = 1
    cnt = 1

    for i in point:
        for j in range(len(point_sum)):
            if visited[i+point_sum[j]] == 0:
                visited[i+point_sum[j]] = 1
                point_sum.append(i+point_sum[j])
                cnt += 1

    print(f'#{tc} {cnt}')






