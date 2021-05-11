import sys
# 1번부터 N번까지의 구역
# 두개의 선거구로 나누며, 각 구역은 두 선거구 중 하나에 포함되어야 함
# 한 선거구에 포함된 구역들은 서로 연결되어 있어야한다.

# 두개의 선거구로 나누는 법은 nC1...nC n//2 까지
# 하나의 선거구가 서로 연결되었는지는 인접리스트 dfs ??


def linked(tr, cnt_p):
    if len(tr) == 1:
        return True

    stack = [tr[0]]
    cnt_p += p_count[tr[0]]     # 해당 지역구의 사람수를 더하는 중...
    tr.remove(tr[0])        # tr[0] 값을 지우고 싶은건데 이렇게 하면 stack의 인덱스 참고 값이 변할까...? 노노 확인해봤는데 안변했어
    while stack:
        node = stack.pop()
        for nb in adj_list[node]:     # 현재 노드와 연결된 이웃들 중에서
            if nb in tr:
                stack.append(nb)
                tr.remove(nb)

    # 그렇게 이웃된 것들을 모두 확인하고 tr에서 remove 했는대도 아직 tr이 남아있다?? => 하나의 선거구가 연결되어 있는 것이 아니다.
    if tr:
        return False

    return True

def comb(n, r):
    if r == 0:
        linked(tr, 0)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

input = sys.stdin.readline
N = int(input())
p_count = list(map(int, input().split()))

adj_list = [[] for _ in range(N)]
for _ in range(N):
    temp = list(map(int, input().split()))
    adj_list[_].extend(temp[1:])


an = [i for i in range(1, N+1)]
for r in range(1, (N//2)+1):
    tr = [0] * r
    comb(N, r)

