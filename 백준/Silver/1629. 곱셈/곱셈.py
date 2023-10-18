import sys

input = sys.stdin.readline

def power(A, B, C):
  if B == 0:
    return 1
  
  if B == 1:
    return A % C

  pow = power(A, B//2, C)

  if B % 2:
    return pow * pow * A % C
  else:
    return pow * pow % C
  
A, B, C = map(int, input().split())

print(power(A, B, C))