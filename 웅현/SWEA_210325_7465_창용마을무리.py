def BFS():
    global stack, pointer, result
    if pointer > N:
        return

    group = []
    stack.append(pointer)
    while len(stack) != 0:
        tmp = stack.pop(-1)
        if not visited[tmp]:
            visited[tmp] = True
            group.append(tmp)
            for w in adjacency[tmp]: # 인접한 대상을 stack에 쌓는다.
                if not visited[w]:
                    stack.append(w)
    # stack이 비어지면 이곳으로 온다. 다음 사람을 조사해야 한다.
    if len(stack) == 0 and len(group) > 1:
        pointer += 1 # 다음 사람 조사.
        result += 1
    else:
        pointer += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 창용마을 사람 수, M은 서로를 알고 있는 사람의 관계 수 ( 간선의 개수 )
    visited = [False] * (N + 1)
    adjacency = []
    for i in range(N+1):
        adjacency.append([])
    for i in range(M):
        p1, p2 = map(int, input().split()) # 관계가 있는 사람.
        adjacency[p1].append(p2)
        adjacency[p2].append(p1)

    pointer = 1 # pointer는 1부터 N까지이다.
    stack = []
    result = 0 # 무리 개수를 세기 위한 변수

    while pointer != N:
        BFS()

    print(f'#{tc} {result}')







