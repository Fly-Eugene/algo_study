
# for tc in range(1, 11):
#     N = int(input())
#
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     res = 0
#     for c in range(N):
#         idx = 0
#         stop = 0
#         while True:
#             if idx == N-1:
#                 break
#             elif arr[idx][c] == 1: # N 발견
#                 for r in range(idx+1, N):
#                     if arr[r][c] == 2:  # 교착상태 발견
#                         res += 1
#                         idx = r+1
#                         if idx >= N-1: stop = 1
#                         break
#                     elif r == N-1:  # 끝까지 갔는데 발견 못함
#                         stop = 1
#                         break
#             else: idx += 1
#
#             if stop == 1: break # 끝가지 갔는데 발견 못함 => 그 뒤로 볼 필요 없음
#
#     print(f'#{tc} {res}')

def magnetic(lst):
    S, cnt = [], 0
    while lst:
        top = lst.pop()
        if top == 1: # 1 이면 밖으로 나가려함. 2가 스택안에있으면 2랑 부딪
            if S:
                S.pop()
                cnt += 1
        elif top == 2:
            S.append(top)
    return cnt


for t in range(1, 2):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    retable = [[table[j][i] for j in range(N)] for i in range(N)]

    ans = 0
    for i in range(N):
        ans += magnetic(retable[i])
    print('#{} {}'.format(t, ans))

# 7
# 1 0 2 0 1 0 1
# 0 2 0 0 0 0 0
# 0 0 1 0 0 1 0
# 0 0 0 0 1 2 2
# 0 0 0 0 0 1 0
# 0 0 2 1 0 2 1
# 0 0 1 2 2 0 2