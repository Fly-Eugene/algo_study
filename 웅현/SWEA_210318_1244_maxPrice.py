T = int(input())
for tc in range(1, T+1):
    boards, N = input().split()

    answer = list(boards)
    answer = list(map(int, answer))
    answer.sort(reverse=True)

    origin = list(boards)
    origin = list(map(int, origin))

    check = [False] * len(origin)
    for i in range(len(origin)):
        if origin[i] == answer[i]:
            check[i] = True





