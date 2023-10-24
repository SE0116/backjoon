import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(start):
  
  for i in node_list[start]:
    if not visited[i]:
      visited[i] = visited[start] + 1
      dfs(i)
  

n = int(input())
first, second = map(int, input().split())
m = int(input())
node_list = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  node_list[x].append(y)
  node_list[y].append(x)

visited = [False] * (n+1)


dfs(first)
print(-1) if visited[second] == 0 else print(visited[second])