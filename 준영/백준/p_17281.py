from sys import stdin
# pypy라도 플래티넘 문제부터는 위험해진다고 한다.
# pypy는 재귀에 약하다고 한다. 재귀를 피할 수 있으면 피하자
def p_set(idx):
    # global을 많은 걸 해주면 조금 더 빠르다
    global sco, m_sco, N
    if idx == 9:
        sco = 0
        p_now = 0
        for i in range(N):
            out = 0
            # 배열 대신 변수 세개를 선언하는게 더 빠르다
            p1, p2, p3 = 0, 0, 0
            while out < 3:
                shot = arr[i][sel[p_now]]
                if shot == 4:
                    # sum을 쓰면 더 느려진다
                    sco += p1 + p2 + p3 + 1
                    # 배열을 새로 선언해주는 것 보다, g = [0,0,0]
                    # 배열안의 값을 변경하는 것이 더 빠르고, g[0], g[1], g[2]= 0,0,0
                    # 그것보다는 아예 배열을 안쓰는게 더 빠르다 p1, p2, p3 = 0, 0, 0
                    p1, p2, p3 = 0, 0, 0
                elif shot == 3:
                    sco += p1 + p2 + p3
                    p1, p2, p3 = 0, 0, 1
                elif shot == 2:
                    sco += p3 + p2
                    p1, p2, p3 = 0, 1, p1
                elif shot == 1:
                    sco += p3
                    p1, p2, p3 = 1, p1, p2
                else:
                    out += 1

                p_now += 1
                p_now %= 9
            # 불가능 조건은 걸어주는 것이 더 빠르다
            if sco + (N - i - 1) * 24 < m_sco:
                break
        # 직접 구현보다 max 쓰는 것이 더 빠르다
        m_sco = max(m_sco, sco)
        return
    # 조건을 걸 때는 for문 바깥에 조건을 거는게 조금 더 빠르다
    if idx == 3:
        idx += 1
    for i in range(9):
        if check[i] == 0:
            sel[idx] = i
            check[i] = 1
            p_set(idx + 1)
            check[i] = 0

# 인풋은 readline으로 바꾸는게 조금 빠르다
N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [0] * 9
sel = [0] * 9
sco, m_sco = 0, 0
check[0] = 1
p_set(0)
print(m_sco)