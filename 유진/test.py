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

    # 디버깅
    # if pang_order == [2, 2, 6]:
    #     print('base')
    #     for _ in range(len(simulation_block)):
    #         print(simulation_block[_])
    #     print('---------------')

    for col in pang_order:
        top = len(simulation_block[col])-1
        if top > 0:
            removed = pang(col, top, simulation_block, 0)

            # 디버깅
            # if pang_order == [2, 2, 6]:
            #     print('before')
            #     for _ in range(len(simulation_block)):
            #         print(simulation_block[_])
            #     print('---------------')

            if removed == 0:
                return 0
            # simulation_block 에서 0 제거후 반복
            for k in range(W-1, -1, -1):
                for l in range(len(simulation_block[k])-1, -1, -1):
                    if simulation_block[k][l] == 0:
                        simulation_block[k].pop(l)

        # 디버깅
        # if pang_order == [2, 2, 6]:
        #     print('after')
        #     for _ in range(len(simulation_block)):
        #         print(simulation_block[_])
        #     print('---------------')

    # 남은 블록갯수 카운팅 후 리턴
    result = sum(1 for blocks in simulation_block for block in blocks if block)
    return result


def perm(r):
    pick = [0] * r

    def making(idx, pick):
        global ans
        if ans == 0:
            return
        if idx == r:
            # print(pick)
            simulation = [list(brick_stack[_]) for _ in range(W)]
            min_bricks = repeat_pang(pick, simulation)
            if min_bricks < ans:
                ans = min_bricks
            return

        for i in range(W):
            pick[idx] = i
            making(idx+1, pick)

    making(0, pick)


for t in range(1, int(input())+1):
    N, W, H = map(int, input().split())         # N: 구슬개수, W: 가로, H: 세로
    brick_stack = [[] for _ in range(W)]
    bricks = [list(map(int, input().split())) for h in range(H)]

    for h in range(H-1, -1, -1):
        for w in range(W):
            if bricks[h][w]:
                brick_stack[w].append(bricks[h][w])

    ans = W * H
    perm(N)
    print(f'#{t} {ans}')

