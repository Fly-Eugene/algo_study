import sys
sys.stdin = open('SWEA_1486_장훈이.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    ## N명, 선반의 높이 = B
    N, B = map(int, input().split())
    h_list = list(map(int, input().split()))

    ## 부분집합을 이용해 B 이상이면서 가장 작은 수 구하기
    # ans = []
    min_num = 987654321
    for i in range(1<<N):
        res = 0
        for j in range(N):
            if i & (1<<j):
                res += h_list[j]

        if B <= res < min_num:
            min_num = res

    ## B를 넘으면서 가장 작은 값과 B의 차이값 구하기
    diff = min_num - B

    print(f'#{tc} {diff}')
