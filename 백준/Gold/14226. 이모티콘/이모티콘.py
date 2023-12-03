from collections import deque
import sys
input = sys.stdin.readline


S = int(input())

queue = deque([(1, 0)])
visited = [[-1] * (S+1) for _ in range(S+1) ]
visited[1][0] = 0
result = -1

while queue:
  imti, cnt = queue.popleft()
  if visited[imti][imti] == -1:
    visited[imti][imti] = visited[imti][cnt] + 1
    queue.append((imti, imti))

  if imti + cnt <= S and visited[imti + cnt][cnt] == -1:
    visited[imti + cnt][cnt] = visited[imti][cnt] + 1
    queue.append((imti + cnt, cnt))
  
  if imti - 1 >= 0 and visited[imti-1][cnt] == -1:
    visited[imti-1][cnt] = visited[imti][cnt] + 1
    queue.append((imti-1, cnt))

for i in range(S+1):
  if visited[S][i] != -1:
    if result == -1 or result > visited[S][i]:
      result = visited[S][i]
      
print(result)