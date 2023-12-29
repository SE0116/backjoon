import sys
input = sys.stdin.readline


N = int(input())

if N == 1:
  exit()

while N > 1:
  for divisor in range(2, N + 1):
    if not N % divisor:
      print(divisor)
      N //= divisor
      break