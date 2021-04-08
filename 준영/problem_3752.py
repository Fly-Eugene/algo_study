for tc in range(1, int(input()) + 1):
    N = int(input())  # 문제 수
    scores = list(map(int, input().split()))  # 정해진 배점을 따른다
    res = set()
    arr = [1, 2, 3]

    res.add(0)
    for score in scores:
        for item in set(res):
            res.add(score + item)

    print("#{} {}".format(tc, len(res)))
