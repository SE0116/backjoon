import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def dfs(y, x):
  # 해당 지점 방문처리
  island[y][x] = -1
  
  # 가로, 세로, 대각선 탐색 후 방문하면 -1로 방문처리
  for i in range(8):
    y_dy, x_dx = y + dy[i], x + dx[i]
    if 0 <= y_dy < h and 0 <= x_dx < w and island[y_dy][x_dx] == 1:
      dfs(y_dy, x_dx)

  return 1


while True:
  w, h = map(int, input().split())
  if w == h == 0:
    break

  island = []
  for _ in range(h):
    island.append(list(map(int, input().split())))
  
  # 가로, 세로, 대각선 탐색용 좌표
  dy, dx = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
  cnt = 0

  # 값이 1인 위치만 탐색해서 DFS 호출
  for row in range(h):
    for col in range(w):
      if island[row][col] == 1:
        cnt += dfs(row, col)

  print(cnt)