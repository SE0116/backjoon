import sys
sys.stdin.readline

# 원하는 범위 내에 0이 있는지 확인하는 함수
def check(y, x, num):

  # 3x3 크기의 정사각형 내 인덱스 검색용 변수
  dy = y // 3 * 3
  dx = x // 3 * 3

  for i in range(9):
    #가로줄 탐색  
    if number_place[y][i] == num:
      return False
    
    #세로줄 탐색
    if number_place[i][x] == num:
      return False

    # 3x3 정사각형 탐색
    if number_place[dy + (i // 3)][dx + (i % 3)] == num:
      return False

  return True
  

def dfs(idx):
  # 0이 다 채워졌으면 출력하고 종료
  if idx == len(zero):
    for i in range(9):
      print(*number_place[i])
    exit()
    
  # 탐색하려는 곳의 좌표로 초기화
  y, x = zero[idx]

  for i in range(1, 10):
    # i가 가로 / 세로 / 정사각형 안에 없으면 i 저장하고 다음 인덱스로
    if check(y, x, i):
      number_place[y][x] = i
      dfs(idx + 1)
      # 백트래킹으로 다시 돌아오면 0으로 초기화
      number_place[y][x] = 0


number_place = []
for _ in range(9):
  number_place.append(list(map(int, input().split())))

# 스도쿠 판에서 값이 0인 위치들 저장
zero = []
for i in range(9):
  for j in range(9):
    if number_place[i][j] == 0:
      zero.append((i, j))

dfs(0)