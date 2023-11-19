import sys
input = sys.stdin.readline


N = int(input())

if N == 4 or N == 7:
  print(-1)

elif N % 5 == 0:
  print(N // 5)

elif N % 5 == 1:
  print(2+1+(N//5-2))

elif N % 5 == 2:
  print(4+0+(N//5-2))

elif N % 5 == 3:
  print(1+2+(N//5-2))

elif N % 5 == 4:
  print(3+1+(N//5-2))