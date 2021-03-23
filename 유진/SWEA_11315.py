## 내가 생각한 풀이방법 ##
# 리스트로 데이터프레임 생성

import random
import sys
from pandas import Series, DataFrame

sys.stdin = open('SWEA_11315.txt', 'r')

T = int(input())

for test in range(1, T+1):
    N = int(input())

    # 기본값 설정
    df_list = []
    result = "NO"

    # 리스트로 입력받아 데이터 프레임 생성하기
    for i in range(N):
        N_list = []
        five_stones = input()
        for stone in five_stones:
            N_list.append(stone)
            df_list.append(N_list)


    df = DataFrame(df_list)

    # df.iloc을 사용한다.
    # 가로 연속성 확인하기
    for i in range(N):
        cnt_a = 0
        for j in range(N):
            if df.iloc[i, j] == 'o':
                cnt_a += 1
                # 만약 cnt_a가 5이상이면
                if cnt_a >= 5:
                    result = "YES"
                    break
            else:
                cnt_a = 0

    # 세로 연속성 확인하기
    for i in range(N):
        cnt_b = 0
        for j in range(N):
            # 가로와의 j, i 위치가 바꼈다.
            if df.iloc[j, i] == 'o':
                cnt_b += 1
                # 만약 cnt_b가 5이상이면
                if cnt_b >= 5:
                    result = "YES"
                    break
            else:
                cnt_b = 0

    # ################## 대각선 연속성 확인하기 ###############
    #
    # # 왼.아 => 오.위 대각선 역속성 확인하기
    # large_x_a = 4
    # large_y_a = 0
    # cnt_c_a = 0
    #
    # # 왼.아 => 오.위 대각선 왼쪽에서 중심까지의 모음
    # while large_x_a <= N-1:
    #     small_x_a = large_x_a
    #     small_y_a = large_y_a
    #     # 하나의 대각선줄을 확인하는 while 문
    #     while small_x_a >= 0:
    #         if df.iloc[small_x_a, small_y_a] == 'o':
    #             cnt_c_a += 1
    #
    #             # 만약 cnt_c가 5 이상이라면
    #             if cnt_c_a == 5:
    #                 result = "YES"
    #                 break
    #         else:
    #             cnt_c_a = 0
    #         small_x_a -= 1
    #         small_y_a += 1
    #     large_x_a += 1
    #
    # # 왼.아 => 오.위 대각선 중심부터 오른쪽까지의 모음
    #
    # large_x_b = N-1
    # large_y_b = N-5
    # cnt_c_b = 0
    #
    # while large_y_b >= 1:
    #     small_x_b = large_x_b
    #     small_y_b = large_y_b
    #
    #     while small_y_b <= N-1:
    #         if df.iloc[small_x_b, small_y_b] == 'o':
    #             cnt_c_b += 1
    #
    #             if cnt_c_b == 5:
    #                 result = "YES"
    #                 break
    #             else:
    #                 cnt_c_b = 0
    #         small_x_b -= 1
    #         small_y_b += 1
    #     large_y_b -= 1
    #
    #
    # # 왼.위 => 오.아 대각선 왼쪽부터 중심까지의 모음
    # large_x_c = 0
    # large_y_c = N-5
    # cnt_c_c = 0
    #
    # while large_y_c >= 0:
    #     small_x_c = large_x_c
    #     small_y_c = large_y_c
    #
    #     while small_y_c <= N-1:
    #         if df.iloc[small_x_c, small_y_c] == 'o':
    #             cnt_c_c += 1
    #
    #             if cnt_c_c == 5:
    #                 result = "YES"
    #                 break
    #             else:
    #                 cnt_c_c = 0
    #         small_x_c += 1
    #         small_y_c += 1
    #     large_y_c -= 1
    #
    #
    # # 왼.위 => 오.아 대각선 중심부터 오른쪽까지의 모음
    # large_x_d = 1
    # large_y_d = 0
    # cnt_c_d = 0
    #
    # while large_x_d <= N-5:
    #     small_x_d = large_x_d
    #     small_y_d = large_y_d
    #
    #     while small_x_d <= N-1:
    #         if df.iloc[small_x_d, small_y_d] == 'o':
    #             cnt_c_d += 1
    #
    #             if cnt_c_d == 5:
    #                 result = "YES"
    #                 break
    #             else:
    #                 cnt_c_d = 0
    #         small_x_d += 1
    #         small_y_d += 1
    #     large_x_d += 1

    print(f'#{test} {result}')