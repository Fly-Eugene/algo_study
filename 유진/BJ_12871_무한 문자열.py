# def BruteForce(total, pattern):
#     i = 0
#     j = 0
#     while i < N:
#         if total[i] != pattern[j]:
#             return 0
#         i += 1
#         j += 1
#         # 하나의 패턴이 완성됐다?? 그럼 다시 pattern index는 0으로
#         if j == M-1:
#             j = 0
#             i += 1
#
#             # total 문자의 끝까지 패턴과 일치한다.(패턴의 반복이 total 문자열이다)
#             if i == N:
#                 return 1
#
# s = input()
# t = input()
#
# ## 어떤게 더 짧은 문자열인지 확인하기 => 짧은 문자열 == pattern
# if len(s) < len(t):
#     pattern = s
#     total = t
# else:
#     pattern = t
#     total = s
#
# N = len(total)
# M = len(pattern)
#
# res = BruteForce(total, pattern)
#
# print(f'{res}')


s = input()
t = input()

if len(s) <= len(t):
    p = len(s)
    t = len(t)
else:
    p = len(t)
    t = len(s)

