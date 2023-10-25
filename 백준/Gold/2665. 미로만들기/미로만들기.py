import sys, heapq
input = sys.stdin.readline


n = int(input())

maze_list = []
for _ in range(n):
  maze_list.append(list(map(int, input().strip())))
  
visited =[[False] * n for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x):
  cnt = 0
  queue = []
  heapq.heappush(queue, (cnt, y, x))
  visited[y][x] = True

  while queue:
    
    cnt, y, x = heapq.heappop(queue)

    if y == x == n-1:
      print(cnt)
      return

    for i in range(4):
      y_dy = y + dy[i]
      x_dx = x + dx[i]
      
      # 벽 만나면 뚫어버리고 cnt + 1
      if 0 <= y_dy < n and 0 <= x_dx < n and visited[y_dy][x_dx] == False:
        visited[y_dy][x_dx] = True
        if maze_list[y_dy][x_dx] == 0:
          heapq.heappush(queue, (cnt+1, y_dy, x_dx))
        else:
          heapq.heappush(queue, (cnt, y_dy, x_dx))


bfs(0, 0)