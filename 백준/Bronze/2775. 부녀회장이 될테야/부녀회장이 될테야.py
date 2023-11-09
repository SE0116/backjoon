import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  k = int(input())
  N = int(input())

  citizen = [i for i in range(1, N+1)]
  
  for i in range(k):
    for j in range(1, N):
        citizen[j] += citizen[j-1]

  print(citizen[-1])