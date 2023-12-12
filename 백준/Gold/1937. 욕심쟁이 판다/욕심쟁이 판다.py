import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def panda(y, x):
  # 이미 탐색한 위치면 해당 위치의 값 그대로 반환
  if check_list[y][x]:
    return check_list[y][x]
  
  check_list[y][x] += 1

  # 상하좌우 탐색
  for i in range(4):
    y_dy, x_dx = y + dy[i], x + dx[i]
    if 0 <= y_dy < n and 0 <= x_dx < n and bamboo[y_dy][x_dx] > bamboo[y][x]:
      check_list[y][x] = max(check_list[y][x], panda(y_dy, x_dx) + 1)
      
  return check_list[y][x]


n = int(input())

bamboo = []
for _ in range(n):
  bamboo.append(list(map(int, input().split())))

max_eat = 0
check_list = [[0] * n for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

for row in range(n):
  for col in range(n):
    max_eat = max(max_eat, panda(row, col))

print(max_eat)