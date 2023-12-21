from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

queue = deque()
queue.append((N, 0))
visited = [0] * (N + 1)

while queue:
  N, cnt = queue.popleft()
  if N == 1:
    print(cnt)
    break

  if not N % 3 and not visited[N % 3]:
    queue.append((N // 3, cnt + 1))
    visited[N // 3] = 1

  if not N % 2 and not visited[N % 2]:
    queue.append((N // 2, cnt + 1))
    visited[N // 2] = 1

  if not visited[N - 1]:
    queue.append((N - 1, cnt + 1))
    visited[N - 1] = 1
