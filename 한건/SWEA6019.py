import sys
sys.stdin = open('SWEA6019_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    NN, D = input().split()
    N = int(NN)
    lst = [list(map(int, input().split())) for _ in range(N)]

    print('원본')
    for a in lst:
        print(a)
    print('--------------------')
    if D == 'up':
        for i in range(N):
            for j in range(N):
                if i < N - 2 and lst[i][j] == lst[i + 1][j]:
                    lst[i + 1][j] = 0
                    lst[i][j] *= 2
                if i < N - 2:
                    ci = i
                    while lst[i][j] == 0:
                        lst[i][j] = lst[ci + 1][j]
                        lst[ci + 1][j] = 0
                        ci += 1
                    if 0 < i and lst[i][j] == lst[i - 1][j]:
                        lst[i][j] = 0
                        lst[i - 1][j] *= 2
    if D == 'right':
        pass
    if D == 'down':
        pass
    if D == 'left':
        pass

    for k in lst:
        print(k)
    break
