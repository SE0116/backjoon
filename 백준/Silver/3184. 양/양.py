from collections import deque
import sys
input = sys.stdin.readline


def bfs(y, x):
  global sheep, wolf
  s_cnt, w_cnt = 0, 0

  # 해당 영역에 양이나 늑대가 있는지 확인
  if yard[y][x] == 'v':
    w_cnt += 1
  elif yard[y][x] == 'o':
    s_cnt += 1

  # 탐색이 끝난 지역은 헷갈리지 않게 '.'으로 바꿔놓기
  yard[y][x] = '.'
  visited[y][x] = True
  queue.append((y, x))

  while queue:
    y, x = queue.popleft()
    
    if yard[y][x] == 'v':
      w_cnt += 1
    elif yard[y][x] == 'o':
      s_cnt += 1
  
    yard[y][x] = '.'

    for i in range(4):
      y_dy, x_dx = y + dy[i], x + dx[i]
      # 울타리 안쪽에서만 탐색하게 범위 허용
      if 0 <= y_dy < R and 0 <= x_dx < C and yard[y_dy][x_dx] != '#' and not visited[y_dy][x_dx]:
        visited[y_dy][x_dx] = True
        queue.append((y_dy, x_dx))

  # 한 구역에 양이 더 많으면 그 구역의 늑대는 전부 쫓아내고
  # 늑대가 더 많으면 양을 전부 잡아먹음
  if s_cnt > w_cnt:
    w_cnt = 0
  else:
    s_cnt = 0

  sheep += s_cnt
  wolf += w_cnt  

R, C = map(int, input().split())

yard = []
for _ in range(R):
  yard.append(list(map(str, input().rstrip())))

sheep, wolf = 0, 0
queue = deque()

# 방문여부 확인용 배열
visited = [[False] * C for _ in range(R)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

# 마당 탐색
for row in range(R):
  for col in range(C):
    if yard[row][col] == 'v' or yard[row][col] == 'o':
      bfs(row, col)

print(sheep, wolf)