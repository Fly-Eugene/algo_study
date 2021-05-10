dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def pang(col, top, simulation_block, cnt):
    if cnt == H * W:
        return 0
    power = simulation_block[col][top]
    simulation_block[col][top] = 0
    if power:
        cnt += 1
    if power >= 2:
        for k in range(1, power):
            for j in range(4):
                ncol, ntop = col + dc[j] * k, top + dr[j] * k
                if 0 <= ncol < W and 0 <= ntop < len(simulation_block[ncol]) \
                        and simulation_block[ncol][ntop]:
                    pang(ncol, ntop, simulation_block, cnt)
        return cnt
    else:
        return cnt


# 맞은 벽돌 깨지는것 구현
def repeat_pang(pang_order, simulation_block):
    for col in pang_order:
        top = len(simulation_block[col])-1
        if top >= 0:
            removed = pang(col, top, simulation_block, 0)
            if removed == 0:
                return 0
            # simulation_block 에서 0 제거후 반복
            for k in range(W-1, -1, -1):
                for l in range(len(simulation_block[k])-1, -1, -1):
                    if simulation_block[k][l] == 0:
                        simulation_block[k].pop(l)


    # 남은 블록갯수 카운팅 후 리턴
    result = sum(1 for blocks in simulation_block for block in blocks if block)
    return result


def perm(lst, r):
    visited = [0 for _ in range(len(lst))]
    pick = [0] * r

    def making(idx, pick, visited):
        global ans
        if ans == 0:
            return
        if idx == r:
            simulation = [list(brick_stack[_]) for _ in range(W)]
            min_bricks = repeat_pang(pick, simulation)
            if min_bricks < ans:
                ans = min_bricks
            return

        for i in range(len(lst)):
            if not visited[i] and (i == 0 or lst[i-1] != lst[i] or visited[i-1]):
                pick[idx] = lst[i]
                visited[i] = 1
                making(idx+1, pick, visited)
                visited[i] = 0
                pick[idx] = 0
    making(0, pick, visited)


for t in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    sel = [0] * N
    brick_stack = [[] for _ in range(W)]
    bricks = [list(map(int, input().split())) for h in range(H)]
    for h in range(H-1, -1, -1):
        for w in range(W):
            if bricks[h][w]:
                brick_stack[w].append(bricks[h][w])
    # 쌓아올린 이중리스트 형식의 스택 벽돌
    lst = [i for i in range(W) for _ in range(len(brick_stack[i]))]
    ans = W * H
    perm(lst, N)
    print(f'#{t} {ans}')


