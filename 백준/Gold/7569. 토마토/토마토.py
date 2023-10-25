from collections import deque
import sys
input = sys.stdin.readline


def bfs():  
  
  while queue:
    z, y, x = queue.popleft()
    for i in range(6):
      z_dz, y_dy, x_dx = z + dz[i], y + dy[i], x + dx[i]
      # 좌표가 지정 범위를 벗어나지 않았을 때
      # 다음 토마토를 queue에 추가해주고
      # 이전 queue에 있던 수치에 +1 (토마토가 전부 익는데 걸린 시간도 같이 계산)
      if 0 <= z_dz < H and 0 <= y_dy < N and 0 <= x_dx < M and tomato_list[z_dz][y_dy][x_dx] == 0:
        queue.append((z_dz, y_dy, x_dx))
        tomato_list[z_dz][y_dy][x_dx] = tomato_list[z][y][x] + 1
        

M, N, H = map(int, input().split())

tomato_list = []
for _ in range(H):
  tomato_list.append([list(map(int, input().split())) for _ in range(N)])

queue = deque()

# 하루가 지나면 주변 토마토가 한번에 익기 때문에 1 근처의 0인 토마토를 전부 queue에 저장
for z in range(H):
  for y in range(N):
    for x in range(M):
      if tomato_list[z][y][x] == 1:
        queue.append((z, y, x))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

day = 0

bfs()

# 탐색이 끝나면 안익은 토마토가 있는지 확인
# tomato_list[z]
for i in tomato_list:
  
  # tomato_list[z][y]
  for j in i:

    #tomato_list[z][y][x]
    for k in j:

# 안익은 토마토가 있으면 -1
      if k == 0:
        print(-1)
        exit()
    
    # 한 줄의 토마토가 다 익었으면 값이 가장 큰 토마토와 일수를 비교해 큰 수로 저장
    day = max(day, max(j))

# 시작할 때 익은 토마토가 1이였기 때문에 마지막 결과에서 -1
print(day-1)