from collections import deque
import sys
input = sys.stdin.readline


def bfs(y, x, top):
  queue = deque()
  queue.append((y, x, top))
  visited[y][x] = True
  cnt = 1

  while queue:
    y, x, top = queue.popleft()
    visited[y][x] = True

    for i in range(4):
      y_dy, x_dx = y + dy[i], x + dx[i]

      # 1. 현재 좌표가 지역을 벗어나지 않고 
      # 2. 비에 잠기지 않고
      # 3. 이전에 방문한 적이 없고
      # 4. 큐에 들어간 적이 없는 지역이면 append
      if 0 <= x_dx < N and 0 <= y_dy < N and rain_list[y_dy][x_dx] > top and not visited[y_dy][x_dx] and (y_dy, x_dx, top) not in queue:
        queue.append((y_dy, x_dx, top))
        cnt += 1

  return cnt



N = int(input())

rain_list = []
max_num = 0

for i in range(N):
  rain_list.append(list(map(int, input().split())))
  if max(rain_list[i]) > max_num:
    max_num = max(rain_list[i])

# 잠긴 영역이 몇 군데인지 확인용 cnt
result = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


for num in range(max_num):
  visited = [[False] * N for _ in range(N)]
  cnt_list = []

  for i in range(N):
    for j in range(N):
      if rain_list[i][j] > num and not visited[i][j]:
        cnt_list.append(bfs(i, j, num))

  result.append(len(cnt_list))

print(max(result))