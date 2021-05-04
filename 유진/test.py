
## 중복 순열...? 을 만들어 보려고 한다.
def perm(idx):

    if idx == 3:
        print(sel)
        return      # 제발!!! return 좀 하자하자!!!

    for i in range(4):
        sel[idx] = i
        perm(idx+1)

        # sel[idx] = 0

sel = [0]*3
perm(0)