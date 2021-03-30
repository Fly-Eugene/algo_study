
N = int(input())
arr = list(map(int, input().split()))
res = 0

# 버블정렬로 시간 정렬하기
for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# 하나씩 더해주기
for i in range(N):
    res += arr[i] * (N-i)

print(f'{res}')
