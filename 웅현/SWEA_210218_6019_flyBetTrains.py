T = int(input())

for tc in range(1, T+1):
    values = list(map(int, input().split()))
    dist = values[0] # 두 기차 사이의 거리
    velo_a = values[1]/3600 # 기차 A의 거리. 이 때 주의해야 할 점은 시속이라는 점이다.
    velo_b = values[2]/3600 # 기차 B의 거리
    velo_fly = values[3]/3600 # 파리의 이동 속도
    dist_fly = 0 # 시간당 파리가 이동한 거리
    result = 0

    while dist > 0:
        # 시간 당 두 기차 사이의 거리는 시간당 두 기차의 속도를 더한만큼 감소한다.

        dist -= (velo_a + velo_b)

        # dist_fly는 임시값이다.
        result += velo_fly
        dist_fly += velo_fly
        if dist_fly == dist: # 두 기차 사이의 남은 거리가 파리가 이동한 거리와 같다는 뜻이다.
            dist_fly = 0

    result = round(result, 7)
    print(f'#{tc} {result}')