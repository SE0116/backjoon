import sys
input = sys.stdin.readline


n = int(input())

if n == 1 or n == 3:
  print(-1)

elif n % 5 == 1:
  print(3 + n//5 - 1)

elif n % 5 == 2:
  print(1 + n//5)

elif n % 5 == 3:
  print(4 + n//5 - 1)

elif n % 5 == 4:
  print(2 + n//5)

else:
  print(n//5)