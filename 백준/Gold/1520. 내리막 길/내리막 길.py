import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def down(y, x):
  if y == M-1 and x == N-1:
    return 1

  # 이미 갔던 곳이면 그 장소에 저장된 끝 지점까지의 경우의 수 반환
  if visited[y][x] != -1:
    return visited[y][x]

  # 경우의 수 저장용 변수
  cnt = 0

  # 4방향 탐색
  for i in range(4):
    y_dy, x_dx = y + dy[i], x + dx[i]
    # y, x가 지도를 벗어나지 않고 다음 가려는 지점이 현재 지점보다 작은 값일 때
    if 0 <= y_dy < M and 0 <= x_dx < N and map_list[y][x] > map_list[y_dy][x_dx]:
      # 재귀로 들어가서 끝 지점까지 도착하면 cnt에 +1
      cnt += down(y_dy, x_dx)
  
  # 여기까지 쌓인 cnt를 현재 y, x좌표에 저장
  visited[y][x] = cnt
  return visited[y][x]


M, N = map(int, input().split())

map_list = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[-1] * N for _ in range(M)]

for _ in range(M):
  map_list.append(list(map(int, input().split())))

print(down(0, 0))

# down(0, 0)
# print(visited[0][0])
