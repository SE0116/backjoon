import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  a, b = map(int, input().split())

  if b % 4 == 0:
    b = 4
  else:
    b %= 4
  
  if (a**b) % 10 == 0:
    print(10)
  else:
    print((a**b)%10)