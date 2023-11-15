import sys
sys.stdin.readline


n = int(input())

wine_list = [0]
for _ in range(n):
  wine_list.append(int(input()))

dp_list = [0] * (n+1)

#포도주가 2개 이하일 때
if n <= 2:
  print(sum(wine_list))

else:
  dp_list[1] = wine_list[1]
  dp_list[2] = wine_list[1] + wine_list[2]

  for i in range(3, n + 1):
    # 1. 현재 인덱스의 포도주를 마시지 않을 때 (이전까지의 양까지만)
    # 2. 바로 직전의 포도주를 마시지 않았을 때
    # 3. 직전과 이번 포도주를 다 마셨을 때
    # 의 최댓값 비교
    dp_list[i] = max(dp_list[i-3] + wine_list[i-1] + wine_list[i], dp_list[i-2] + wine_list[i], dp_list[i-1])
  print(dp_list[-1])