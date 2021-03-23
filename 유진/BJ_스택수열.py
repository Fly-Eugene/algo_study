
N = int(input())
ans = [int(input()) for _ in range(N)]      # 원하는 수열

arr = []        # push하면 들어갈 리스트
new_arr = []    # pop하면 들어갈 리스트

res = []        # push, pop(+, -) 을 기록할 리스트

num = 1
ans_idx = 0
while len(new_arr) != N:

    if num < ans[ans_idx]:  # 수열의 값보다 작으면 계속 push
        arr.append(num)      # push
        res.append('+')
        num += 1

    elif num == ans[ans_idx]:
        res.append('+')

        new_arr.append(num)
        res.append('-')

        num += 1
        ans_idx += 1

    elif num > ans[ans_idx]:
        if arr[-1] == ans[ans_idx]:  # push
            new = arr.pop()

            new_arr.append(new)
            res.append('-')

            ans_idx += 1
        else:
            res = 'NO'
            break

if res == 'NO':
    print(res)
else:
    for i in range(len(res)):
        print(res[i])