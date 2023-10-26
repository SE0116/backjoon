from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

virus_list = []
queue = []

for i in range(N):
  virus_list.append(list(map(int, input().split())))
  for j in range(N):  
    if virus_list[i][j] != 0:
      queue.append((virus_list[i][j], i, j))


time, target_y, target_x = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = 0

queue.sort()

queue = deque(queue)

while queue:
  loof = len(queue)
  if cnt == time:
    break

  for _ in range(loof):
    
    virus_num, y, x = queue.popleft()
    
    for i in range(4):
      y_dy = y + dy[i]
      x_dx = x + dx[i]

      if 0 <= y_dy < N and 0 <= x_dx < N:
        if virus_list[y_dy][x_dx] == 0:
          virus_list[y_dy][x_dx] = virus_num
          queue.append((virus_num, y_dy, x_dx))

  cnt += 1
  
print(virus_list[target_y-1][target_x-1])