
# M 만큼 for문을 돌면서 각각 A, B 위치를 갱신
# A, B가 위치한 곳이 동일한 BC 충전 가능성이 있을 때
# => 둘이 같은 BC에 위치해 반띵하는게 좋을지, 아니면 따로 BC해서 충전하는게 나을지 선택해야됨
# 주어진 배열에서 행열이 바뀌어 있다는 것을 주의한다.

move = {0: [0, 0], 1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1]}    # 각 move에 대한 dr, dc

for tc in range(1, int(input())+1):
    M, A = map(int, input().split())
    move_a = [0] + list(map(int, input().split()))
    move_b = [0] + list(map(int, input().split()))

    # arr = [[]*10 for _ in range(10)]
    charge_list = []
    for idx in range(A):
        j, i, c, p = map(int, input().split())    # j,i : 열,행  c: 충전 범위, p: 충전가능량
        j, i = j-1, i-1
        charge_list.append((i, j, c, p, idx))

    # print('충전소 위치는', charge_list)

    ar, ac = 0, 0       # A 이동자의 초기값
    br, bc = 9, 9
    sum_charge = 0

    for m in range(M+1):  # M번의 이동을 거치면서
        a_charge = []  # 해당 위치에서 a가 충전가능한 충전소 / 해당 충전소의 power
        b_charge = []
        max_charge = 0

        # A, B 이동자가 충전할 수 있는 충전소를 체크한다.
        a_dr, a_dc = move[move_a[m]]
        ar, ac = ar + a_dr, ac + a_dc

        b_dr, b_dc = move[move_b[m]]
        br, bc = br + b_dr, bc + b_dc

        for charge in charge_list:
            dist_a = abs(ar-charge[0]) + abs(ac-charge[1])
            dist_b = abs(br-charge[0]) + abs(bc-charge[1])

            if dist_a <= charge[2]: # 만약 charge의 중심부와의 거리가 c보다 작거나 같으면
                a_charge.append(charge[4])  # charge_idx를 append한다.

            if dist_b <= charge[2]:
                b_charge.append(charge[4])

        # print('현재 move', m)
        # print('a 이동자가 충전 가능', a_charge)
        # print('b 이동자가 충전 가능', b_charge)

        # a, b permutation
        # a, b 각각 하나만 리스트가 있을 경우 따로 처리
        if a_charge and b_charge:
            for a in a_charge:
                for b in b_charge:
                    if a == b:
                        if max_charge < charge_list[a][3]:
                            max_charge = charge_list[a][3]
                    else:
                        if max_charge < (charge_list[a][3] + charge_list[b][3]):
                            max_charge = charge_list[a][3] + charge_list[b][3]

        elif a_charge and not b_charge:
            for a in a_charge:
                if max_charge < charge_list[a][3]:
                    max_charge = charge_list[a][3]

        elif b_charge and not a_charge:
            for b in b_charge:
                if max_charge < charge_list[b][3]:
                    max_charge = charge_list[b][3]

        # print('최대 충전', max_charge)
        sum_charge += max_charge

    print(f'#{tc} {sum_charge}')
