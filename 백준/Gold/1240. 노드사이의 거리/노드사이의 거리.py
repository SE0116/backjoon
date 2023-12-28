from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]

# 인접 리스트
for _ in range(N-1):
  node1, node2, dist = map(int, sys.stdin.readline().split())
  node[node1].append((node2, dist))
  node[node2].append((node1, dist))

# BFS
for _ in range(M):
  node1, node2 = map(int, input().split())
  
  queue = deque()
  visited = [False for _ in range(N+1)]

  queue.append((node1, 0))

  while queue:
    now, dist = queue.popleft()
    
    visited[now] = True

    if now == node2:
      print(dist)  
      break

    else:
      for next, next_dist in node[now]:
        if not visited[next]:
          queue.append((next, next_dist + dist))
