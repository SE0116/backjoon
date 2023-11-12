import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(y, x):
  for i in range(4):
    y_dy, x_dx = y + dy[i], x +  dx[i]

    # 다음 좌표가 방문하지 않은 곳이면 더 깊게 탐색하기
    if 0 <= y_dy < N and 0 <= x_dx < M and baechu[y_dy][x_dx] == 1:
      baechu[y_dy][x_dx] = -1
      dfs(y_dy, x_dx)
  

T = int(input())

for i in range(T):
  
  M, N, K = map(int, input().split())

  baechu = [[0] * M for _ in range(N)]

  # 필요한 지렁이 양
  worm = 0

  for i in range(K):
    col, row = map(int, input().split())
    baechu[row][col] = 1

  # 좌표 탐색용 배열
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

  # dfs로 탐색하지 않은 좌표면 시작지점을 방문한 것으로 표시하고(-1) 새로 진입
  for row in range(N):
    for col in range(M):
      if baechu[row][col] == 1:
        baechu[row][col] = -1
        dfs(row, col)
        
        worm += 1

  print(worm)