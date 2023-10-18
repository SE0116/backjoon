import sys
input = sys.stdin.readline


num_city = int(input())

pay_list = [list(map(int, input().split())) for _ in range(num_city)]


# 최소값을 구하는 문제기 때문에 최대값으로 초기화
min_pay = int(1e9)

# 방문 경로를 저장할 배열 생성 (인덱스 호출용)
dist = []

# 방문 경로를 visited를 통해 체크
visited = [False] * num_city  

# 백트래킹
def tsp(idx, pay):
  global min_pay

  # 최종 선택까지 도착해서 다음 비용이 0이 아니고 (처음 지역으로 돌아갈 수 있고)
  # 총 비용이 현재 최소값보다 적으면 기록 갱신
  if idx == num_city:
    if pay_list[dist[num_city-1]][dist[0]] != 0:
      min_pay = min(min_pay, pay + pay_list[dist[idx-1]][dist[0]])
    return
  
  for i in range(num_city):
    # 1. 시작지점이거나
    # 2. 아직 방문하지 않은 지역이거나
    # 3. 이동하려는 지역까지 비용이 0이 아니거나
    # 4. 이동비용이 현재 최소값보다 작으면
    # dist에 어디로 이동하는지 저장 후 다음 지역을 찾기 위해 재귀로 진입 -> 함수가 끝나고 돌아오면 저장한 인덱스와 방문기록 삭제
    if idx == 0 or (not visited[i] and pay_list[dist[idx-1]][i] != 0 and min_pay > pay):
      dist.append(i)
      visited[i] = True
      tsp(idx + 1, pay + pay_list[dist[idx-1]][i])
      dist.pop()
      visited[i] = False

tsp(0, 0)
print(min_pay)