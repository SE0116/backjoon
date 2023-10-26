from collections import deque
import sys
input = sys.stdin.readline

def bfs(y, x):
  queue = deque()
  queue.append((y, x))
  visited[y][x] = True
  cnt = 1
  
  while queue:
    y, x = queue.popleft()
    visited[y][x] = True

    for i in range(4):
      y_dy, x_dx = y + dy[i], x + dx[i]

      if 0 <= y_dy < N and 0 <= x_dx < N and not visited[y_dy][x_dx] and house_list[y_dy][x_dx] == 1 and (y_dy, x_dx) not in queue:
        queue.append((y_dy, x_dx))
        cnt += 1
    
  return cnt

N = int(input())

house_list = []

for i in range(N):
  house_list.append(list(map(int, input().strip())))

size_list = []

visited = [[False] * (N+1) for _ in range(N+1)]
  
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
  for j in range(N):
    if house_list[i][j] != 0 and not visited[i][j]:
      size_list.append(bfs(i, j))

size_list.sort()
print(len(size_list))
for i in range(len(size_list)):
  print(size_list[i])