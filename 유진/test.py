import copy

# 구슬을 던지는 가능한 모든 경우의 수를 구하는 함수.
def solution(string, hit_count):
    #  구슬을 쏘는 곳에 대한 완전 탐색 실시..
    # '0000' 와 같은 스트링 형태로 구슬을 던질 col을 결정한다.
    a = 0
    global result
    if hit_count > N:
        result.add(string)
        return
    else:
        for col in range(W):
            solution(string + str(col), hit_count + 1)



# 각 col 별로 가장 위 point를 기록
def check_top(col):
    for row in range(H):
        if bricks[row][col] != 0:
            return row
    # 한 줄의 모든 벽돌이 0인 경우
    return False


# 구슬을 쏘는 함수.
def fire(string):
    for shoot in string:
        # 구슬을 던질 열에서, 가장 위에 위치하는 point를 계산하자.
        point_row = check_top(int(shoot))
        # 연쇄 작용으로 벽돌 부수기. 단, 구슬을 쏘았을 때 충돌하는 벽돌이 없는 경우에는 넘어간다.
        if point_row:
            r = bricks[point_row][int(shoot)]
            bomb(point_row, int(shoot), r) # TypeError 발생... ㅠㅠㅠㅠㅠ


# visited랑 dfs를 활용한다면 중복 코드를 줄일 수 있다!
# 연쇄 작용으로 벽돌을 깨는 함수
def bomb(row, col, r):
    dr = [-r, +r, 0, 0]
    dc = [0, 0, -r, +r]
    for way in range(4):
        if way == 0:
            move_to_row = range(row, row + dr[way], -1)
        else:
            move_to_row = range(row, row + dr[way])
        if way == 2:
            move_to_col = range(col, col + dc[way], -1)
        else:
            move_to_col = range(col, col + dc[way])
        # row 방향에 대해서 벽돌 깨기
        for i in move_to_row:
            if 0 <= i & i < H:
                if i == row: # 자기 자신은 그냥 깨고
                    bricks[i][col] = 0
                elif bricks[i][col] <= 1: # 값이 1이거나 0인 대상은 0으로 변환하고
                    bricks[i][col] = 0
                else: # 1보다 큰 대상인 경우, 주변의 연쇄 작용을 고려한다.
                    bomb(i, col, bricks[i][col])
        # col 방향에 대해서 벽돌 깨기
        for j in move_to_col:
            if 0 <= j & j < W:
                if j == col:
                    bricks[row][j] = 0
                elif bricks[row][j] <= 1:
                    bricks[row][j] = 0
                else:
                    bomb(row, j, bricks[row][j])

    # 벽돌을 모두 깼으면 정리해주자.
    # col 방향으로 0이 아닌 숫자의 개수를 세서, 모두 0으로 초기화 하고 값을 다시 넣어준다.
    for col in range(W):
        fall(col)


# 벽돌 정리하는 함수.
def fall(col):
    col_numbers = []
    for row in range(H):
        if bricks[row][col] != 0:
            col_numbers.append(bricks[row][col])
        # 값에 상관없이 0으로 초기화 한다.
        bricks[row][col] = 0
    # 아래에서부터 채워야 하므로, 뒤집어준다.
    col_numbers.reverse()
    # col_numbers의 길이만큼 아래에서부터 채워준다.
    idx = 0
    row = H-1

    while idx < len(col_numbers):
        bricks[row][col] = col_numbers[idx]
        idx += 1
        row -= 1


# 모든 구슬을 발사한 후, 남아있는 벽돌의 개수를 계산한다.
def count_bricks():
    bcount = 0
    for row in range(H):
        for col in range(W):
            if bricks[row][col] != 0:
                bcount += 1
    return bcount


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    bricks_tmp = copy.deepcopy(bricks)
    result = set()
    min_val = 1620

    solution('', 0)
    for way in result:
        # 구슬을 던지기 전에, bricks를 초기화 해줘야 한다.
        bricks = copy.deepcopy(bricks_tmp)
        fire(way)
        # 구슬을 모두 던진 후, 남아 있는 벽돌의 개수를 계산
        after_fire = count_bricks()
        if after_fire < min_val:
            min_val = after_fire

    print(f'#{tc} {min_val}')