from collections import deque
import sys
input = sys.stdin.readline


# subway : 입력받을 노선 정보
# cycle : 순환선 확인용 subway 복사본
# branch : 각 역의 인접한 역의 갯수
# parent : 인접한 역
N = int(input())
subway = [[] for _ in range(N+1)]
cycle = [[] for _ in range(N+1)]
branch = [0] * (N+1)
parent = [-1] * (N+1)
result = [-1] * (N+1)

for _ in range(N):
  start, end = map(int, input().split())
  subway[start].append(end)
  subway[end].append(start)

  cycle[start].append(end)
  cycle[end].append(start)

  branch[start] += 1
  branch[end] += 1

# 순환선 찾아내기 ( 순환선이 아닌 역들 지우기 )
while 1 in branch:
  for i in range(1, N+1):
    # 인접한 역이 한 개면 순환선일 수 없으니까
    # 해당 역을 지우고 인접한 역의 정보 변경
    if branch[i] == 1:
      parent[i] = cycle[i][0]
      branch[i] = 0
      branch[parent[i]] -= 1
      
      cycle[i].pop()
      cycle[parent[i]].remove(i)

# BFS로 순환선 이외의 역들까지의 거리 탐색
queue = deque()

# 위에서 탐색이 되지 않은 역은 순환선이기 때문에 거리를 0으로 초기화
for i in range(1, N+1):
  if parent[i] == -1:
    result[i] = 0
    queue.append(i)

# 각 역 사이의 가중치는 1이기 때문에 이전의 역까지의 거리에 +1 더하기
while queue:
  station = queue.popleft()

  for next in subway[station]:
    if result[next] == -1:
      result[next] = result[station] + 1
      queue.append(next)

print(*result[1:])