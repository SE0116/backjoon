from collections import deque
import sys
input = sys.stdin.readline


def dfs(start):
  global cnt, check
  visited[start] = True
  
  if A[start-1] == '1':
    check += 1

  if check == 2:
    cnt += 1
    check -= 1
    return
  
  for i in node_list[start]:
    if visited[i] == False:
      dfs(i)


N = int(input())
A = list(map(str, input().strip()))

node_list = [[] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
  u, v = map(int, input().split())
  node_list[u].append(v)
  node_list[v].append(u)

cnt = 0

for i in range(1, N+1):
  visited = [False] * (N+1)
  if A[i-1] == '1':
    check = 0
    dfs(i)
  
print(cnt)