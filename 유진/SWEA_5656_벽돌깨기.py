# N은 최대 4개, N * W 만큼의 구슬을 떨어트릴 수 있는 경우의 수가 발생
# 폭발을 연쇄적으로 일으켜야한다.
# 그리고 또 남은 애들을 밑으로 가라앉혀야 함..

## 난 block을 인자로 넣으면 굉장히 메모리를 많이 잡아먹을거라고 생각해서
## 일부러 복사하고 다시 재할당하는 과정을 많이 거쳤다... 근데 이 과정이 너무 많이 반복되는거라면
## 차라리 인수로 넣자...

import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def drop(temp_block):
    # 폭발 후 남은 숫자들을 stack에 넣는다.
    stack = [[] for _ in range(W)]
    for r in range(H):
        for c in range(W):
            if temp_block[r][c]:
                stack[c].append(temp_block[r][c])

    # stack을 이용해 블럭들을 내린다.
    # print(stack)
    return_block = [[0] * W for _ in range(H)]
    for w in range(W):
        h = H-1
        while stack[w]:
            item = stack[w].pop()
            return_block[h][w] = item
            h -= 1

    return return_block


def bomb_bfs(r, c, temp_block):
    queue = [(r, c)]

    # 연쇄 폭발하기
    while queue:
        r, c = queue.pop(0)
        # print(r,c, temp_block[r][c])

        for i in range(4):  # 상하좌우 4방향 이니까
            for j in range(temp_block[r][c]-1):
                nr = r + dr[i]*(j+1)
                nc = c + dc[i]*(j+1)

                if 0 <= nr < H and 0 <= nc < W:
                    # print('현재', nr, nc, '를 체크하고 있어요', temp_block[nr][nc])
                    if temp_block[nr][nc] == 1:
                        temp_block[nr][nc] = 0
                    elif temp_block[nr][nc] >= 2:  # 벽돌의 위력이 2 이상이면?
                        # print(nr, nc, '는 2이상인 자리에요')
                        queue.append((nr, nc))

        temp_block[r][c] = 0

    # 벽돌 밑으로 떨어트리는 과정
    return_block = drop(temp_block)

    return return_block

def perm_rep(idx, block):
    global min_cnt     # 여기서 temp_block을 반드시 global 변수로 선언을 해줘야 한다...

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
        temp_block = copy.deepcopy(block)
        for h in range(H):
            if temp_block[h][w]:
                temp_block = bomb_bfs(h, w, temp_block)
                break
        perm_rep(idx+1, temp_block)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().rstrip().split())
    block = [list(map(int, input().rstrip().split())) for _ in range(H)]


    ## 중복 순열을 구현한다.
    min_cnt = W*H
    perm_rep(0, block)

    print(f'#{tc} {min_cnt}')

