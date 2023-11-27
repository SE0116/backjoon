import sys
input = sys.stdin.readline


# 두 점 사이의 거리 계산
def dist(coor1, coor2):
  return (coor2[0] - coor1[0]) ** 2 + (coor2[1] - coor1[1]) ** 2

def dnc(start, end):
  # 점이 한 개면 최솟값을 구하는 문제기 때문에 최대치 반환
  if start == end:
    return sys.maxsize
  
  # 두 점이 붙어있으면 거리 반환
  if end - start == 1:
    return dist(coordinate[start], coordinate[end])
  
  # 중간에 다른 점이 있으면 중간 지점을 계산해서 재귀호출
  mid = (start + end) // 2
  min_dist = min(dnc(start, mid), dnc(mid, end))

  # 중간 지점 기준으로 최솟값 비교할 배열 생성
  check = []

  # 이전에 최솟값보다 작은 범위의 영역만 계산해서
  # 그 안의 값들을 check에 저장
  for i in range(start, end + 1):
    if (coordinate[mid][0] - coordinate[i][0]) ** 2 < min_dist:
      check.append(coordinate[i])

  # min_dist 범위 내의 값들만 y좌표 기준 정렬
  check.sort(key = lambda x : x[1])

  # 가장 작은 y부터 시작해서 대소비교
  # 만약 가장 높은 점에 가기 전에 최솟값보다 큰 값이 나오면 그 위에 있는 점들까지의 거리도 무조건 크기 때문에 break
  for i in range(len(check) - 1):
    for j in range(i + 1, len(check)):
      if (check[i][1] - check[j][1]) ** 2 < min_dist:
        min_dist = min(min_dist, dist(check[i], check[j]))
      else:
        break
      
  # 최종 최솟값 반환
  return min_dist


n = int(input())

coordinate = []
for _ in range(n):
  x, y = map(int, input().split())
  coordinate.append((x, y))

# 중복되는 값 처리
coordinate = sorted(list(coordinate))

print(dnc(0, len(coordinate) - 1))