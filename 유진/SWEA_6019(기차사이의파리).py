import sys
sys.stdin = open('SWEA_6019.txt', 'r')

T = int(input())

for test in range(1, T+1):

    D, A, B, F = map(int, input().split())
    result = 0

    while D >= 10**(-6):
        # 파리가 B를 향해 날아갈 때
        t1 = D / (F + B)  # 파리가 B를 향해 날아가 부딪힌 시간
        D = D - (A*t1 + B*t1)  # 파리가 B에 부딪힌 시간에 새로운 A, B사이 거리 갱신
        result += F*t1  # 파리가 날아간 거리 result에 추가

        # 피리가 다시 A를 향해 날아갈 때
        t2 = D / (F + A) # 파리가 A를 향해 날아가 부딪힌 시간
        D = D - (A*t2 + B*t2) # 새로운 거리 갱신
        result += F*t2 # 파리가 날아간 거리 result에 추가

    print(f'#{test} {result}')





