from collections import deque
import sys
sys.stdin.readline


def bfs(y, x):
  # 시작 위치를 -1로 해서 방문한 것으로 설정
  # check : 그림의 크기
  queue.append((y, x))
  art[y][x] = -1
  check = 1

  while queue:
    y, x = queue.popleft()
    
    # 상하좌우로 탐색해야 하니까 반복문 4번
    for i in range(4):
      y_dy, x_dx = y + dy[i], x + dx[i]

      # 1. 도화지를 벗어나지 않고
      # 2. 아직 그림의 크기를 다 재지 않았으면 ( 1이 남아있으면 )
      # 3. queue에 넣고 다음 그림칸 -1로 저장, 크기 1 늘리기
      if 0 <= y_dy < n and 0 <= x_dx < m and art[y_dy][x_dx] == 1:
        queue.append((y_dy, x_dx))
        art[y_dy][x_dx] = -1
        check += 1

  return check


n, m = map(int, input().split())

art = []
for _ in range(n):
  art.append(list(map(int, input().split())))

queue = deque()
cnt = 0
max_art = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 아직 본 적 없는 그림칸만 ( -1, 0이 아닌 부분만 ) 탐색해서 최대 크기인 그림만 max_art에 저장
for row in range(n):
  for col in range(m):
    if art[row][col] == 1:
      max_art = max(max_art, bfs(row, col))
      cnt += 1

print(cnt, max_art, sep='\n')