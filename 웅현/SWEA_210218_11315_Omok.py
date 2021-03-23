T = int(input())

for tc in range(1, T+1):
    size = int(input())
    answer = "NO"

    # 바둑판의 크기만큼 입력을 받아야한다.
    grid = [list(input()) for i in range(size)]


    for i in range(len(grid)):
        if answer == "YES": break
        for j in range(len(grid[i])): # N x N 이므로 의미는 없다.
            if answer == "YES" : break

            cnt = 0
            if grid[i][j] == 'o':
                cnt = 1
                # 가로 방향 검사
                right = j + 1 # 오른쪽으로 한칸 이동한 것.
                while right < len(grid[i]):
                    if grid[i][right] == 'o':
                        cnt += 1
                        right += 1
                    else:

                        break

                    if cnt == 5:
                        answer = "YES"
                        break
                # 여기에 왔다는 건, 위의 while문에서 cnt가 5개인 오목을 찾을수 없었다는 것을 뜻한다.
                cnt = 1

                # 세로 방향 검사
                down = i + 1
                while down < len(grid):
                    if grid[down][j] == 'o':
                        cnt += 1
                        down += 1
                    else:
                        break

                    if cnt == 5:
                        answer = "YES"
                        break
                cnt = 1

                # 대각선 방향 검사 : 오른쪽 아래 방향
                dr = i + 1
                dc = j + 1
                while dr < len(grid[i]) and dc < len(grid):
                    if grid[dr][dc] == 'o':
                        cnt += 1
                        dr += 1
                        dc += 1
                    else:
                        break

                    if cnt == 5:
                        answer = "YES"
                        break
                cnt = 1

                # 대각선 방향 검사 : 오른쪽 위 방향 검사
                dr2 = i - 1
                dc2 = j + 1
                while 0 <= dr2 and dc2 < len(grid):
                    if grid[dr2][dc2] == 'o':
                        cnt += 1
                        dr2 -= 1
                        dc2 += 1
                    else:
                        cnt = 1
                        break

                    if cnt == 5:
                        answer = "YES"
                        break

    print(f'#{tc} {answer}')