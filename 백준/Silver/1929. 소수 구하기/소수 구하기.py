import sys
input = sys.stdin.readline


M, N = map(int, input().split())
result = []

for i in range(M, N+1):
  if i == 1:
    continue

  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      break
  else:
    result.append(i)
  
print(*result, sep='\n')