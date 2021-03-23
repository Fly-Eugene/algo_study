T = int(input())

for test in range(T):

    N = int(input())
    test_list = list(map(int, input().split()))
    count_list = [0] * 101

    for test in test_list:
        count_list[test] += 1

    max_count = 0
    max_idx = 0

    for i in range(len(count_list)):
        if count_list[i] >= max_count:
            max_count = count_list[i]
            max_idx = i

    print(f'#{N} {max_idx}')