import sys
input = sys.stdin.readline


N, M = map(int, input().split())

DBJ = {}
result = []

for _ in range(N+M):
  name = input().strip()
  if name not in DBJ:
    DBJ[name] = 1
  else:
    DBJ[name] += 1

  if DBJ[name] == 2:
    result.append(name)

result.sort()
print(len(result), *result, sep='\n')
