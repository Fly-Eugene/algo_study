
T = int(input())

for tc in range(1, T+1):
    N, dir = input().split()
    N = int(N)

    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[0]*N for _ in range(N)]

    if dir == 'left':
        for i in range(N):
            idx = 0         # 현재 arr을 체크해줄 idx
            add_idx = 0     # new_arr에 추가해줄 idx
            while idx <= N-1:
                # 현재 위치가 마지막이고 0이 아니면
                if idx == N-1 and arr[i][idx] != 0:
                    new_arr[i][add_idx] = arr[i][idx]
                    idx += 1
                    add_idx += 1

                # 현재 위치가 0이면
                elif arr[i][idx] == 0:
                    idx += 1

                # 내뒤의 숫자와 다르면
                elif arr[i][idx] != arr[i][idx+1]:
                    new_arr[i][add_idx] = arr[i][idx]
                    idx += 1
                    add_idx += 1

                # 내 뒤의 숫자와 같으면 합한다.(= *2 한다)
                elif arr[i][idx] == arr[i][idx+1]:
                    new_arr[i][add_idx] = arr[i][idx] * 2
                    idx += 2
                    add_idx += 1

    elif dir == 'right':
        for i in range(N):
            idx = N-1
            add_idx = N-1
            while 0 <= idx:
                # 현재 위치가 맨 왼쪽이면
                if idx == 0:
                    new_arr[i][add_idx] = arr[i][idx]
                    idx -= 1
                    add_idx -= 1

                # 현재 위치 값이 0 이면
                elif arr[i][idx] == 0:
                    idx -= 1

                # 한칸 왼쪽이랑 값이 다르면
                elif arr[i][idx] != arr[i][idx-1]:
                    new_arr[i][add_idx] = arr[i][idx]
                    idx -= 1
                    add_idx -= 1
                
                # 한칸 오른쪽이랑 값이 같으면
                elif arr[i][idx] == arr[i][idx-1]:
                    new_arr[i][add_idx] = arr[i][idx] * 2
                    idx -= 2
                    add_idx -= 1

    elif dir == 'up':
        for j in range(N):
            idx = 0
            add_idx = 0
            while idx <= N-1:
                if idx == N-1 and arr[idx][j] != 0:
                    new_arr[add_idx][j] = arr[idx][j]
                    add_idx += 1
                    idx += 1
                elif arr[idx][j] == 0:
                    idx -= 1
                elif arr[idx][j] != arr[idx+1][j]:
                    new_arr[add_idx][j] = arr[idx][j]
                    add_idx += 1
                    idx += 1
                elif arr[idx][j] == arr[idx+1][j]:
                    new_arr[add_idx][j] = arr[idx][j] * 2
                    add_idx += 1
                    idx += 2

    elif dir == 'down':
        for j in range(N):
            idx = N-1
            add_idx = N-1
            while 0<= idx:
                if idx == 0 and arr[idx][j] != 0:
                    new_arr[add_idx][j] = arr[idx][j]
                    add_idx -= 1
                    idx -= 1
                elif arr[idx][j] == 0:
                    idx -= 1
                elif arr[idx][j] != arr[idx-1][j] and arr[idx][j] != 0:
                    new_arr[add_idx][j] = arr[idx][j]
                    add_idx -= 1
                    idx -= 1
                elif arr[idx][j] == arr[idx-1][j]:
                    new_arr[add_idx][j] = arr[idx][j] * 2
                    add_idx -= 1
                    idx -= 2

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])