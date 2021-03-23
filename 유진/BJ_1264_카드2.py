
N = int(input())
card = [i for i in range(1, N+1)]
card.extend([0]*2*N)

i = 0
last = N   # 카드번호가 있는 마지막 인덱스

while True:
    if card[i+1] != 0:
        if card[i] >= 1 and i % 2 == 0:   # 현재 실행중인 순서가 홀수이면
            card[i] = -1 # 카드 번호를 없는 카드로 설정
            i += 1

        elif card[i] >= 1 and i % 2 == 1:
            tmp = card[i]  # 맨 앞장의 카드를 빼서
            card[i] = -1
            card[last] = tmp    # 다시 맨 뒤에 넣는다.
            i += 1
            last += 1
    elif card[i+1] == 0:
        res = card[i]
        break
    print(card)

print(res)





