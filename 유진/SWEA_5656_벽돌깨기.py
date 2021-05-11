# N은 최대 4개, N * W 만큼의 구슬을 떨어트릴 수 있는 경우의 수가 발생
# 폭발을 연쇄적으로 일으켜야한다.
# 그리고 또 남은 애들을 밑으로 가라앉혀야 함..

## 난 block을 인자로 넣으면 굉장히 메모리를 많이 잡아먹을거라고 생각해서
## 일부러 복사하고 다시 재할당하는 과정을 많이 거쳤다... 근데 이 과정이 너무 많이 반복되는거라면
## 차라리 인수로 넣자...

import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

## 2. 한 번 폭발한 뒤 벽돌들을 가라앉히는 함수 == drop
def drop(temp_block):
    # 폭발 후 남은 숫자들을 stack에 넣는다.
    stack = [[] for _ in range(W)]
    for r in range(H):
        for c in range(W):
            if temp_block[r][c]:        # 위쪽에 있는 벽돌들부터 stack에 각각 열별로 쌓입니다.
                stack[c].append(temp_block[r][c])

    # stack을 이용해 블럭들을 내린다.
    # print(stack)
    return_block = [[0] * W for _ in range(H)]          # 새로운 백지 배열 생성
    for w in range(W):   # 각 열에 대해서
        h = H-1             # 맨 밑부터 넣어줄 겁니다.
        while stack[w]:
            item = stack[w].pop()
            return_block[h][w] = item
            h -= 1

    return return_block         # 새롭게 만든 배열을 return 해줄겁니다.

## 1. 한 번 폭발을 연쇄적으로 시키는 함수 == bomb_bfs ( bfs를 이용한 연쇄폭발 )
def bomb_bfs(r, c, temp_block):
    queue = [(r, c)]

    # 연쇄 폭발하기
    while queue:
        r, c = queue.pop(0)
        # print(r,c, temp_block[r][c])

        for i in range(4):  # 상하좌우 4방향 이니까
            for j in range(temp_block[r][c]-1):     # 해당 벽돌의 power-1만큼 퍼져나갈거다
                nr = r + dr[i]*(j+1)
                nc = c + dc[i]*(j+1)

                if 0 <= nr < H and 0 <= nc < W:
                    if temp_block[nr][nc] == 1:     # new 벽돌의 power가 1이면, 그냥 0으로 만들어
                        temp_block[nr][nc] = 0
                    elif temp_block[nr][nc] >= 2:  # 벽돌의 위력이 2 이상이면? 새로운 queue에 추가 => 다른 주변 벽돌을 깨트릴테니까
                        queue.append((nr, nc))

        temp_block[r][c] = 0    # 주변 벽돌을 깨트리고 난 후 본인은 0으로 (자신도 폭발한 벽돌이자나)

    # 벽돌 밑으로 떨어트리는 과정
    return_block = drop(temp_block) # 자, 이제 queue 다 돌았고, 중력을 부여해보자

    return return_block

## 3. 어느 열을 깨트릴건지 중복순열을 구현하는 함수 == perm_rep
def perm_rep(idx, block):
    global min_cnt

    if idx == N:
        cnt = 0
        for j in range(W):
            for i in range(H-1, -1, -1):
                if block[i][j] == 0:
                    break
                cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt

        return

    for w in range(W):
        temp_block = copy.deepcopy(block)       # 매번 현재 block을 복사해서 temp_block으로 지정한다.
        for h in range(H):                  # 이제 벽돌중에서 맨 위쪽에 있는 벽돌을 깨트리겠다. (높이: h, 가로는 : w)
            if temp_block[h][w]:
                temp_block = bomb_bfs(h, w, temp_block)     # 복사한 temp_block에 대해서 bomb_bfs ==> 터지고 가라앉은 새로운 배열이 다시 temp_block에 덮어씌워집니다.
                break
        perm_rep(idx+1, temp_block)     # 이렇게 temp_block은 perm_rep으로 다시 들어가면서 새로운 block이 되는거죠


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().rstrip().split())            # 구슬 개수, 너비, 높이
    block = [list(map(int, input().rstrip().split())) for _ in range(H)]        # 벽돌이 쌓인 2차원 배열


    ## 중복 순열을 구현한다.
    min_cnt = W*H
    perm_rep(0, block)   # N=3 일 때, 000, 001, 002 이렇게 깨보는 함수죠...

    print(f'#{tc} {min_cnt}')


## result = sum(1 for i in arr for j in i if j)
