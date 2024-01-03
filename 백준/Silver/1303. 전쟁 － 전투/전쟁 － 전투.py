from collections import deque
import sys
input = sys.stdin.readline


def search(y, x, color):
  # 시작 지점 큐에 넣기
  queue.append((y, x))
  cnt = 1

  army[y][x] = 'X'

  while queue:
    # 큐의 가장 왼쪽에 있는 값 빼기
    y, x = queue.popleft()

    # 현재 좌표에서 네 방향 탐색
    for i in range(4):
      y_dy, x_dx = y + dy[i], x + dx[i]

      # 전쟁터를 안벗어나고 같은 옷을 입고 있으며, 이미 큐에 저장된 좌표가 아닐 때
      if 0 <= y_dy < M and 0 <= x_dx < N and army[y_dy][x_dx] == color and (y_dy, x_dx) not in queue:
        queue.append((y_dy, x_dx))
        army[y_dy][x_dx] = 'X'
        cnt += 1

  return cnt ** 2


N, M = map(int, input().split())

army = []
for _ in range(M):
  army.append(list(input().strip()))

queue = deque()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
blue_total, white_total = 0, 0

for row in range(M):
  for col in range(N):
    if army[row][col] == 'W':
      white_total += search(row, col, 'W')
    if army[row][col] == 'B':
      blue_total += search(row, col, 'B')

print(white_total, blue_total)