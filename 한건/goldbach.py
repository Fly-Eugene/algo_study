import sys
sys.stdin = open('goldbach_input.txt', 'r')

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    s = []
    # 두 소수의 합
    for i in range(2, N + 1):
        if is_prime(i):
            s.append(i)

    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] + s[j] == N:
                ans += 1
    print(ans)




