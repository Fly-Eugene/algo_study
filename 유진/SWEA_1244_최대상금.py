## 첫 자리에서 가장 큰 거랑 자리를 바꾼다.
## 두 번째 자리에서 뒤 인덱스부터 가장 큰 거랑 자리를 바꾼다.

T = int(input())

for tc in range(1, T+1):
    num, N = map(int, input().split())
    num = str(num)
    num_list = []
    for item in num:
        num_list.append(item)

    idx = 0
    while N:
        # 현재 바꿀 지점이 맨 끝이라면 그 전 지점과 바꾸기
        if idx == len(num_list)-1:
            num_list[idx-1], num_list[idx] = num_list[idx], num_list[idx-1]
            N -= 1
            if N == 0: break
            idx = 0

        # 현재 바꿀 지점(맨 앞부터 가장 큰걸로 채워준다는 개념)
        change = num_list[idx]  # 초기화
        change_idx = idx

        # 이제 idx 뒤쪽으로 change 보다 큰 값이 있는지 찾아본다.
        for i in range(idx+1, len(num_list)):
            if num_list[i] >= change:
                change = num_list[i]
                change_idx = i

        # 현재 위치값보다 큰 값을 찾지 못했다면(즉, 현재 위치값이 가장 큰값)
        if change_idx == idx:
            idx += 1

        # 큰 값을 찾았으면 위치 바꾸기
        elif change_idx != idx:
            num_list[idx], num_list[change_idx] = num_list[change_idx], num_list[idx]
            N -= 1
            idx += 1

    ### 가장 큰 값이 여러개일 때 처리해주기
    

    print(f'#{tc}', end=' ')
    print(*num_list, sep='')

















