## 방법1. 재귀
def recursion_fibo(n):

    if n == 1 or n == 2:
        return 1
    else:
        return recursion_fibo(n-1) + recursion_fibo(n-2)


## 방법2. Memoization
topdown = [1, 1]

def topdown_fibo(n):
    # 종료 조건
    if n == 1 or n == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 메모에서 꺼낸다.
    if n < len(topdown):
        return topdown[n]

    # 아직 계산하지 않은 문제라면 점화식 계산을 통해 피보나치 결과 반환
    topdown.append(topdown[n-1] + topdown[n-2])
    return topdown[n]

## 방법3. DP(Dynamic Programming)
bottomup = [0] * 100

def bottomup_fibo(n):
    if n == 1 or n == 2:
        bottomup[n] = 1
        return bottomup[n]

    else:
        for i in range(3, n+1):
            bottomup[i] = bottomup[i-1] + bottomup[i-2]
        return bottomup[n]