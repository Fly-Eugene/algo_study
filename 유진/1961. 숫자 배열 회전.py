
def rotation(arr):
    N = len(arr)
    new_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]   # j, i의 위치를 바꾸면 90도 회전이 된다!!

    return new_arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res1 = rotation(arr)    # 90도
    res2 = rotation(res1)   # 180도
    res3 = rotation(res2)   # 270도

    print(f'{tc}')

    for i in range(N):
        print(*res1[i], sep='', end=' ')    # sep의 사용 기억하기!!
        print(*res2[i], sep='', end=' ')
        print(*res3[i], sep='')             # 이미 개행을 했기 때문에 밑에 또 할 필요가 X

    # print() # 개행을 위함