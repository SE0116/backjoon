import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  # 동전 가지 수
  N = int(input())

  # 동전의 금액 리스트 ( 인덱스 정렬을 위해 맨앞에 +[0] )
  coin_list = [0] + list(map(int, input().split()))
  
  # 목표 금액
  target = int(input())

  # 값 저장용 테이블
  dp_list = [[0] * (target+1) for _ in range(N+1)]
  
  # 0원이 되는 경우는 무조건 나오기 때문에 +1
  for i in range(N+1):
    dp_list[i][0] = 1

  
  for i in range(1, N+1):
    for j in range(1, target+1):
      # 가치가 적은 동전의 경우의 수 가져오기
      dp_list[i][j] = dp_list[i-1][j]
  
      # a원으로 x-a원을 만드는 경우의 수는 (x-a) + a원의 경우의 수와 같다 
      if j >= coin_list[i]:
        dp_list[i][j] += dp_list[i][j - coin_list[i]]

  print(dp_list[N][target])
