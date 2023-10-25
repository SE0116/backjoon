from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

forest_list = []
for _ in range(R):
  forest_list.append(list(input().strip()))


water_queue = deque()
hog_queue = deque()

for i in range(R):
  for j in range(C):
    if forest_list[i][j] == '*':
      water_queue.append((i, j))
    if forest_list[i][j] == 'S':
      hog_queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1

while True:

  for _ in range(len(water_queue)):
    water_y, water_x = water_queue.popleft()
    for i in range(4):
      next_water_y, next_water_x = water_y + dy[i], water_x + dx[i]
      if 0 <= next_water_y < R and 0 <= next_water_x < C :
        if forest_list[next_water_y][next_water_x] == 'X':
          continue

        if forest_list[next_water_y][next_water_x] == 'D':
          continue
        
        if forest_list[next_water_y][next_water_x] == '.':
          forest_list[next_water_y][next_water_x] = '*'
          water_queue.append((next_water_y, next_water_x))
  
  if len(hog_queue) == 0:
    print('KAKTUS')
    break
  for _ in range(len(hog_queue)):
    hog_y, hog_x = hog_queue.popleft()
    for i in range(4):
      next_hog_y, next_hog_x = hog_y + dy[i], hog_x + dx[i]

      if 0 <= next_hog_y < R and 0 <= next_hog_x < C:
      
        if forest_list[next_hog_y][next_hog_x] == 'X':
          continue
        
        if forest_list[next_hog_y][next_hog_x] == '*':
          continue
        if forest_list[next_hog_y][next_hog_x] == '.':
          forest_list[next_hog_y][next_hog_x] = 'S'
          hog_queue.append((next_hog_y, next_hog_x))
        if forest_list[next_hog_y][next_hog_x] == 'D':
          print(cnt)
          exit()
  cnt += 1