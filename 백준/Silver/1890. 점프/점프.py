import sys
input = sys.stdin.readline


N = int(input())

board_list = [(list(map(int, input().split()))) for _ in range(N)]

dp_list = [[0] * N for _ in range(N)]
dp_list[0][0] = 1

for i in range(N):
  for j in range(N): 
    # 시작 지점이 (0, 0)으로 고정이니까 dp테이블값이 0인 지점은 패스
    # 게임판의 값이 0인 경우도 종착점이기 때문에 패스
    if board_list[i][j] != 0 and dp_list[i][j] != 0:
      # 해당 좌표에 저장된 값을 더했을 때 판을 벗어나지 않으면 dp테이블에 합산
      if i + board_list[i][j] < N:
        dp_list[i + board_list[i][j]][j] += dp_list[i][j]
      if j + board_list[i][j] < N:  
        dp_list[i][j + board_list[i][j]] += dp_list[i][j]

print(dp_list[N-1][N-1])