from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

height_list = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for i in range(M):
  u, v = map(int, input().split())
  height_list[u].append(v)
  degree[v] += 1

result = []

def topology():
  global result
  
  queue = deque()
  
  for i in range(1, N + 1):
    if degree[i] == 0:
      queue.append(i)

  while queue:
    idx = queue.popleft()
    result.append(idx)
    
    for i in height_list[idx]:
      degree[i] -= 1

      if degree[i] == 0:
        queue.append(i)
  
  for i in result:
    print(i, end=' ')


topology()
