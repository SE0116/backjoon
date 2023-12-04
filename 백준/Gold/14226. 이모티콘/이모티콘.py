from collections import deque
import sys
input = sys.stdin.readline


S = int(input())

# queue : BFS에 사용할 큐
# visited : 해당 큐에 들어가는 이모티콘( 화면 / 클립보드 둘 다 )의 갯수를 본 적이 있는지 확인하는 배열
# result : 최종 최솟값
queue = deque([(1, 0)])
visited = [[-1] * (S+1) for _ in range(S+1) ]
visited[1][0] = 0
result = sys.maxsize

while queue:
  imti, cnt = queue.popleft()

  # 화면에 있는 이모티콘 클립보드에 복사 ( 1번 연산 )
  if visited[imti][imti] == -1:
    visited[imti][imti] = visited[imti][cnt] + 1
    queue.append((imti, imti))

  # 클립보드에 있는 이모티콘을 복사해도 S를 넘지 않을 때 ( 2번 연산 )
  if imti + cnt <= S and visited[imti + cnt][cnt] == -1:
    visited[imti + cnt][cnt] = visited[imti][cnt] + 1
    queue.append((imti + cnt, cnt))
  
  # 화면에 있는 이모티콘 하나 제거 ( 3번 연산 )
  if imti - 1 >= 0 and visited[imti-1][cnt] == -1:
    visited[imti-1][cnt] = visited[imti][cnt] + 1
    queue.append((imti-1, cnt))

# 너비 우선 탐색으로 찾은 최솟값 찾아내기
for i in range(S+1):
  if visited[S][i] != -1:
    result = min(visited[S][i], result)
    
print(result)