from collections import deque
import sys

input = sys.stdin.readline


N, M = map(int, input().split())

maze_list = [input().strip() for _ in range(N)]
for i in range(len(maze_list)):
  maze_list[i] = list(map(int, maze_list[i]))


def bfs(y, x):
  queue = deque()
  queue.append((y, x))

  while queue:
    y, x = queue.popleft()
  
    # 상하좌우 탐색용 좌표 설정
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]

      # 현재 위치가 미로 밖으로 벗어나면
      if ny < 0 or nx < 0 or ny >= N or nx >= M:
        continue
      
      # 벽에 부딪히면
      if maze_list[ny][nx] == 0:
        continue

      if maze_list[ny][nx] == 1:
        maze_list[ny][nx] = maze_list[y][x] +  1
        queue.append((ny, nx))
  return maze_list[N-1][M-1]
      

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


print(bfs(0, 0))
    

