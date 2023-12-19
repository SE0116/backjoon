import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

# vip_next를 선언 안해주면 vip석이 없을 때 NameError 발생
seats = []
vip_prev, vip_next = 0, 0

# vip석이 나왔을 때 이전까지의 좌석 갯수를 저장
for _ in range(M):
  vip_next = int(input())
  seats.append(vip_next - vip_prev - 1)
  vip_prev = vip_next

# 입력을 다 받고 남은 좌석의 갯수 저장
seats.append(N - vip_next)

# DP용 배열
# dp_list = [0] * (N + 1)
dp_list = [0] * 41

dp_list[0], dp_list[1], dp_list[2] = 1, 1, 2
result = 1

for i in range(3, N + 1):
  dp_list[i] = dp_list[i - 1] + dp_list[i - 2]

for seat in seats:
  if seat == 0:
    continue
    
  result *= dp_list[seat]

print(result)
