import sys
input = sys.stdin.readline


N, M = map(int, input().split())
table = []
dp_list = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
  table.append(list(map(int, input().split())))

# DP용 배열에 미리 각 좌표로 가는 동안의 합 구해놓기
# '- dp_list[i-1][j-1]'의 경우 왼쪽과 위쪽에서 중복으로 계산됐기 때문에 하나 빼주기
for i in range(1, N + 1):
  for j in range(1, N + 1):
    dp_list[i][j] = table[i-1][j-1] + dp_list[i-1][j] + dp_list[i][j-1] - dp_list[i-1][j-1]

# 합을 구할 구간을 입력받고
# 위에서 합을 계산했던 방식의 반대로 계산
for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  result = dp_list[x2][y2] - dp_list[x2][y1-1] - dp_list[x1-1][y2] + dp_list[x1-1][y1-1]

  print(result)
