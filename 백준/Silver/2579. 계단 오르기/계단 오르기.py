import sys
input = sys.stdin.readline

num_stairs = int(input())

stair_list = [0]

for _ in range(num_stairs):
  stair_list.append(int(input()))

dp_list = [0] * (num_stairs+1)

# 계단 수가 2 이하일 때는 다 더한 값이 최댓값
if num_stairs <= 2:
  print(sum(stair_list))

# 계단이 3개 이상일 때는 1, 2번째 계단을 선언해주고 DP 돌리기 (시작지점은 0이니까 할 필요 x)
else:
  dp_list[1] = stair_list[1]
  dp_list[2] = dp_list[1] + stair_list[2]

  for i in range(3, num_stairs+1):
    dp_list[i] = max(dp_list[i-2], dp_list[i-3] + stair_list[i-1]) + stair_list[i]

  print(dp_list[-1])