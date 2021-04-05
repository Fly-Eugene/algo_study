#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = 0      # 소수의 조합 개수를 세는 변수
#
#     for i in range(1, N//2+1, 2):
#         # N을 두 개의 숫자 a,b로 나눌건데 각각 소수인지를 체크하는 변수(0: 소수아님, 1: 소수)
#         a_check = 0
#         b_check = 0
#
#         # 1은 소수가 아니기 때문에 패스
#         if i == 1:
#             continue
#
#         a, b = i, N-i
#
#         for j in range(2, i):
#             # 하나라도 약수가 있으면
#             if a % j == 0:
#                 break
#             if j == a-1:
#                 a_check = 1
#
#         for k in range(2, N-i):
#             # 하나라도 약수가 있으면
#             if b % k == 0:
#                 break
#             if k == b-1:
#                 b_check = 1
#
#         if a_check and b_check:
#             cnt += 1
#
#     print(cnt)

###############################################################

T = int(input())

## 에러토스테네스의 체...??
MAX = 1000000

p = [1] * (MAX+1)

def prime(a):
    for i in range(2, a+1):
        if p[i] == 1:

            # 해당 배수들을 0으로 표시 : 소수가 아니라는 뜻
            j = 2*i
            while j <= a:
                p[j] = 0
                j += i  # i 칸씩 늘려준다 == 배수
        else:
            continue
    return

prime(MAX)

for tc in range(T):
    N = int(input())
    cnt = 0
    for i in range(1, N//2+1, 2):
        if i == 1:
            continue

        if p[i] and p[N-i]:
            cnt += 1
        else:
            continue

    print(cnt)
