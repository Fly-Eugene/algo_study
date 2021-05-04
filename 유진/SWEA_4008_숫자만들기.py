def cal(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    elif op == 3:
        return int(num1 / num2)

def perm(idx, res):
    global max_num, min_num

    if idx == N-1:
        if res < min_num:
            min_num = res
        if res > max_num:       # 여기에 elif 를 두면 어떻게 되겠어?? 나가겠지 ?? 너 바보지??
            max_num = res
        return

    for i in range(4):        # 연산자의 종류는 4종류이다.
        if check[i] != operator[i]:
            check[i] += 1
            perm(idx+1, cal(res, num_list[idx+1], i))
            check[i] -= 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))

    num_list = list(map(int, input().split()))
    min_num, max_num = 100000001, -100000001

    check = [0]*4  # 연산자의 종류는 4개
    perm(0, num_list[0])

    ans = max_num - min_num
    print(f'#{tc} {ans}')
