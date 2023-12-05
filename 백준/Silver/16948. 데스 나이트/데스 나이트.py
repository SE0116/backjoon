from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

r1, c1, r2, c2 = map(int, input().split())

# visited : 데스 나이트가 지나간 자리
visited = [[False] * N for _ in range(N)]
queue = deque([(r1, c1, 0)])

# dr, dc : 데스 나이트가 현재 좌표에서 움직일 수 있는 상대적 거리
dr, dc = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

while queue:
  r, c, cnt = queue.popleft()
  
  # 데스 나이트가 갈 수 있는 좌표면 현재 cnt 수 출력하고 while문 종료
  if (r, c) == (r2, c2):
    print(cnt)
    break

  # 데스 나이트가 움직일 수 있는 경우의 수 탐색
  for i in range(6):
    dr_r, dc_c = r + dr[i], c + dc[i]

    # 데스 나이트가 이동하려는 칸이 체스판을 벗어나지 않고 이전에 갔던 칸이 아니면 cnt를 하나 늘리고 큐에 담기
    if 0 <= dr_r < N and 0 <= dc_c < N and not visited[dr_r][dc_c]:
      visited[dr_r][dc_c] = True
      queue.append((dr_r, dc_c, cnt+1))
      
# break가 걸리지 않았으면, 즉 목표 칸에 도달하지 못하고 큐가 끝나면 -1 출력
else:
  print(-1)