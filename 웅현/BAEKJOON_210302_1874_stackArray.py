N = int(input()) # 1부터 n까지의 정수
stack = []
result = []
arr_list = []
arr_print = []

for i in range(N):
    arr_list.append(int(input()))
pushed_to = 0
factor = True

for number in arr_list:
    # 넣고자 하는 수가 pushed_to보다 작은 숫자이고, 아직 result에 없는 숫자라면? 만들 수 없다.
    if len(stack) > 0 and stack[-1] == number:
        result.append(stack.pop())
        arr_print.append('-')
    if result == arr_list:
        break

    if number < pushed_to and number not in result:
        factor = False
        break

    # 위의 continue 조건을 만족하지 못하는 경우, 이 곳으로 내려온다.
    # 해당 숫자까지 push한다.
    for j in range(pushed_to+1, number+1):
        stack.append(j)
        pushed_to = stack[-1]
        arr_print.append('+')
    if len(stack) > 0:
        if stack[-1] == number:
            result.append(stack.pop())
            arr_print.append('-')

if factor:
    for i in arr_print:
        print(i)
else:
    print('NO')