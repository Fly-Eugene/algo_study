T = int(input())

for tc in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    point_sum = [0] # 가능한 시험 점수를 계속 쌓을 리스트

    visited = [0] * (sum(point) + 1)    # sum(point) + 1 이상의 점수는 존재하지 않는다.
    visited[0] = 1      # 무조건 합이 0인 경우는 존재하니까 1을 넣어줌
    cnt = 1

    for i in point:     # 배점을 다 돌면서
        for j in range(len(point_sum)): # 현재 존재하는 시험점수에
            if visited[i+point_sum[j]] == 0:    # 배점 + 존재하는 시험점수 == 새로운 시험점수 인가? 확인
                visited[i+point_sum[j]] = 1     # 새로운 시험점수라면 ? visited 체크
                point_sum.append(i+point_sum[j])   # 가능한 시험점수 쌓는 리스트에 추가
                cnt += 1    # 갯수 +1

    print(f'#{tc} {cnt}')






