for tc in range(1, 11):
    N, start_i = map(int, input().split()) # 데이터의 길이, 시작점
    arr = list(map(int, input().split())) # 연락망 from-to
    move = [list() for _ in range(101)]  # 연락망 인접리스트
    visited = [0] * 101
    for i in range(0, N, 2):
        move[arr[i]].append(arr[i+1])
    q = []  # 큐
    order_list = []  # 연락받는 사람들을 담기 위한 리스트
    visited[start_i] = 1
    q.append(start_i)
    size = 0
    while len(q):
        size = len(q)
        for i in range(size): # size만큼 돌아야 하나의 거리
            p = q.pop(0)
            for item in move[p]:
                if not visited[item]:
                    visited[item] = 1
                    q.append(item)
                    order_list.append(item)
    # size만큼 뒤에서 자른다
    print('#{} {}'.format(tc, max(order_list[-1:-1-size:-1])))