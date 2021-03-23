import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
  N, direction = input().split()
  print(N, direction)

arr = [map(int, input().split()) for _ in range(N)]

for i in range(N):
  print(arr[i])