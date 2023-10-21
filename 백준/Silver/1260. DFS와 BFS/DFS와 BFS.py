from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 인접행렬 만들기
node_list = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().split())
  node_list[u][v] = node_list[v][u] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(idx):
  visited_dfs[idx] = True

  print(idx, end=' ')

  for i in range(N + 1):
    if visited_dfs[i] == False and node_list[idx][i] == 1:
      dfs(i)


def bfs(idx):
  queue = deque()
  queue.append(idx)

  visited_bfs[idx] = True

  while queue:
    idx = queue.popleft()
    
    print(idx, end=' ')
    
    for i in range(1, N + 1):
      if visited_bfs[i] == False and node_list[idx][i] == 1:
        queue.append(i)
        visited_bfs[i] = True
        


dfs(V)
print()
bfs(V)