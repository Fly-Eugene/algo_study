# 선수들의 순서를 구하고 (순열, permutation) / out 3번 미만까지 점수 계산
def perm(idx):
    global N, score, max_score

    # 9명의 순서가 모두 정해졌다면
    if idx == 9: # 그 9명의 순서가 저장된 sel을 이용해서 각 inning을 돌며 점수를 구한다!!
        score = 0
        i = 0   # sel[i] => 몇번째 선수가 타자인지

        for ing in range(N):
            out = 0
            p1, p2, p3 = 0, 0, 0

            while out < 3:
                if innings[ing][sel[i]] == 4: # 홈런
                    score += p3 + p2 + p1 + 1
                    p1, p2, p3 = 0, 0, 0

                elif innings[ing][sel[i]] == 3:   # 3루타
                    score += p3 + p2 + p1
                    p1, p2, p3 = 0, 0, 1

                elif innings[ing][sel[i]] == 2:   # 2루타
                    score += p3 + p2
                    p1, p2, p3 = 0, 1, p1

                elif innings[ing][sel[i]] == 1:   # 1루타
                    score += p3
                    p1, p2, p3 = 1, p1, p2

                elif innings[ing][sel[i]] == 0:   # 아웃
                    out += 1

                i += 1  # 다음 타자로
                i = i % 9

        max_score = max(score, max_score)
        return

    if idx == 3:  # 1번 선수가 무조건 4번째 타자라서
        idx += 1

    for i in range(9):
        if check[i] == 0:
            sel[idx] = i

            check[i] = 1  # 해당 i 사용했음
            perm(idx+1)
            check[i] = 0

####################################################################################

# 재귀를 이용한 순열을 다시 공부한다고 생각하자!!
N = int(input())   # 게임횟수
innings = [list(map(int, input().split())) for _ in range(N)]

sel = [0] * 9     # innings가 2차니까 똑같이 2차여야 되는거 아니야?
check = [0] * 9   # 아니지, 한 번 순서를 정하면 바꿀 수 없다고 했잖아, 동일한 순서 == 동일한 sel

check[0] = 1 # 1번 선수는 무조건 4번 타자
score, max_score = 0, 0

perm(0)

print(max_score)
