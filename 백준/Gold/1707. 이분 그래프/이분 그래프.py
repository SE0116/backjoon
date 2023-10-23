from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  queue = deque()
  
  queue.append(start)
  
  if visited[start] == 0:
    visited[start] = 1

  while queue:
    
    idx = queue.popleft()
    check = visited[idx]
    
    for i in node_list[idx]:
      if visited[i] == 0:
        queue.append(i)
      
        if check == 1:
          visited[i] = 2
        else:
          visited[i] = 1
      
      elif (visited[i] == 1 and check == 1) or (visited[i] == 2 and check == 2):
        print('NO')
        return False

  return True


K = int(input())

for _ in range(K):
  
  V, E = map(int, input().split())

  check_list = [0] * (V+1)
  node_list = [[] for _ in range(V+1)]
  visited = [0] * (V+1)

  for i in range(E):
    u, v = map(int, input().split())
    node_list[u].append(v)
    node_list[v].append(u)


  for i in range(1, V + 1):
    if not bfs(i):
      break
  else:
    print('YES')