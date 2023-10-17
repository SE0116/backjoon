import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
result = []
people_list = deque([i+1 for i in range(N)])
idx = 0
while people_list:
  if idx % K == K-1:
    result += [people_list.popleft()]
  else:
    people_list.append(people_list.popleft())
  idx += 1

print('<', end='')
for i in range(len(result)):
  if i+1 == len(result):
    print(result[i], end='')
    break
  print(f'{result[i]}, ', end='')
print('>')