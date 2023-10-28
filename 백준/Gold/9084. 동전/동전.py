import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  # 동전 가지 수
  N = int(input())

  # 동전의 금액 리스트
  coin_list = list(map(int, input().split()))
  
  # 목표 금액
  target = int(input())

  # 값 저장용 테이블
  dp_list = [0] * (target+1)
  
  # 0원이 되는 경우는 무조건 나오기 때문에 +1
  dp_list[0] = 1

  for coin in coin_list:
    for i in range(coin, target+1):
      # a원으로 x-a원을 만드는 경우의 수는 (x-a) + a원의 경우의 수와 같다 
      dp_list[i] += dp_list[i-coin]

  print(dp_list[target])
