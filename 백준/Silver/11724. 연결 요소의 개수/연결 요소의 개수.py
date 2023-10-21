import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())

node_list = [[] for _ in range(N + 1)]
for i in range(M):
  u, v = map(int, input().split())
  node_list[u].append(v)
  node_list[v].append(u)

visited = [False] * (N + 1)
cnt = 0

def dfs(idx):
  visited[idx] = True
  
  for i in node_list[idx]:
    if visited[i] == False:
      dfs(i)
    
  

for i in range(1, N + 1):
  if visited[i] == False:
    dfs(i)
    cnt += 1

print(cnt)