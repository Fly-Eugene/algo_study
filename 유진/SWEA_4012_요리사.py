
# 식재료를 각각 N/2개씩 나누어 두 개의 요리를 한다.
# nCn/2 조합의 개수를 생각해야됨;; (power_set? => 부분 집합인데.. 조합은 뭐였지ㅠㅠ)
# 근데 n/2개 뽑은거에서 또 2개씩 조합을 생각해야 됨...?

def powerset(idx, cnt):
    global res, min_diff
    if idx == N:
        return          # return 하는거 잘 챙기기, 알아서 return 되는게 아니다

    if cnt == N//2:     #재료 반으로 가르기
        a_list = []
        b_list = []

        # a재료, b재료 구분하기
        for i in range(N):
            if sel[i] == 1:
                a_list.append(i)
            else:
                b_list.append(i)

        # 각 재료 중에 2개를 선택해서 점수 더하는 과정
        a_ing, b_ing = [], []
        res = 0
        powerset_sub(0, 0, a_list, a_ing)  # a접시 요리중
        a_res = res

        res = 0
        powerset_sub(0, 0, b_list, b_ing)  # b접시 요리중
        b_res = res

        diff = abs(a_res-b_res)
        if diff < min_diff:
            min_diff = diff
        return

    sel[idx] = 1
    powerset(idx+1, cnt+1)
    sel[idx] = 0
    powerset(idx+1, cnt)

# 왜 이렇게 변수가 많은가요? A, B 접시 구할 때 같은 함수를 쓰고 싶은데
# 두 개가 각각 다른 ing_list를 쓰기 때문입니다.
def powerset_sub(idx_sub, cnt_sub, ing_list, ing):
    global res
    if idx_sub == N//2:
        if cnt_sub == 2:    # N//2개 중에 2개의 조합을 볼거임
            ing1, ing2 = ing_list[ing[0]], ing_list[ing[1]]
            res += synergy[ing1][ing2]
            res += synergy[ing2][ing1]
        return

    ing.append(idx_sub)
    powerset_sub(idx_sub+1, cnt_sub+1, ing_list, ing)

    ing.remove(idx_sub)
    powerset_sub(idx_sub+1, cnt_sub, ing_list, ing)

    return 0

###################################################################
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    sel = [0] * N
    res = 0
    min_diff = 20001

    powerset(0, 0)
    print(f'#{tc} {min_diff}')