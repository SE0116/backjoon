import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


N = int(input())

# 인접 리스트
node_list = [[] for _ in range(N+1)]
for i in range(1, N):
  u, v = map(int, input().split())
  node_list[u].append(v)
  node_list[v].append(u)

visited = [False] * (N+1)
parents = [0] * (N+1)

def dfs(idx):
  visited[idx] = True
  
  for i in node_list[idx]:
    if visited[i] == False:
      parents[i] = idx
      dfs(i)

dfs(1)

for i in range(2, len(parents)):
  print(parents[i])