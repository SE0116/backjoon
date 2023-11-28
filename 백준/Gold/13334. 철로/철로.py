import sys, heapq
input = sys.stdin.readline


n = int(input())

pair = []

# 사무실이 집보다 왼쪽에 있을 수도 있기 때문에
# 작은 수를 왼쪽으로 몰기
for _ in range(n):
  h, o = map(int, input().split())
  if h > o:
    pair.append((o, h))
  else:
    pair.append((h, o))

# 끝점 기준 오름차순 정렬 후 시작점이 같으면 시작점 기준 오름차순 정렬
# 시작점을 기준으로 먼저 정렬하면 아래 작성할 while문에서 반례 발생
pair.sort(key=lambda x: (x[1], x[0]))

# dist: 철로의 길이
# queue: 철로 길이 안에 들어갈 수 있는 집과 사무실을 이은 선분들의 집합
dist = int(input())
queue = []
max_queue = 0

# 시작점이 작은 것부터 끝까지 탐색
for i in range(n):
  # 철로의 길이가 집과 사무실 사이 거리보다 길면 queue에 넣기
  if pair[i][1] - pair[i][0] <= dist:
    heapq.heappush(queue, pair[i][0])

  # 철로의 길이보다 집과 사무실 사이 거리가 길면 queue에 들어갈 수 없으니까 continue
  else: 
    continue
  
  # 집과 사무실 기준 끝점에서 현재 queue의 시작점 까지의 거리가 철로의 길이를 벗어나면 queue에서 빼기
  while queue:
    if pair[i][1] - queue[0] > dist:
      heapq.heappop(queue)

    else:
      break

  # queue의 길이가 가장 긴 때를 저장
  max_queue = max(len(queue), max_queue)

print(max_queue)
