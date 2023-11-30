import sys
input = sys.stdin.readline


n = int(input())

enter = {}

for _ in range(n):
  name, status = map(str, input().split())
  if status == 'enter':
    enter[name] = status
  else:
    del enter[name]

result = sorted(enter.keys(), reverse=True)
print(*result, sep='\n')