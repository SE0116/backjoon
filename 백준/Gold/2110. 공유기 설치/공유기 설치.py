import sys
input = sys.stdin.readline


N, C = map(int, input().split())

share = []

for _ in range(N):
  share.append(int(input()))

share.sort()

# 각 집 사이의 최소 및 최대 거리 저장
start, end = 1, share[-1] - share[0]
result = 0

# 이진 탐색
while start <= end:
  # 중간값 선언 ( 공유기 사이의 거리 )
  mid = (start + end) // 2
  now = share[0]
  cnt = 1

  # 현재 거리에서 설치 가능한 공유기의 갯수 구하기
  for i in range(1, N):
    if share[i] >= now + mid:
      cnt += 1
      now = share[i]
    
  # 예상한 공유기 갯수보다 많으면 공유기 사이의 거리 늘리기
  if cnt >= C:
    start, result = mid + 1, mid
  
  # 예상한 공유기 갯수보다 적으면 공유기 사이의 거리 좁히기
  else:
    end = mid - 1

print(result)