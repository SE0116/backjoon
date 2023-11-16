import sys, heapq
input = sys.stdin.readline


N = int(input())

card_list = []

for _ in range(N):
  heapq.heappush(card_list, int(input()))

if N == 1:
  print(0)

else:
  total = 0

  # 두 개씩 pop해서 더한 값을 total에 더하고 그대로 queue에 다시 넣기
  for i in range(N-1):
    
    card_1 = heapq.heappop(card_list)
    card_2 = heapq.heappop(card_list)
        
    total += card_1 + card_2
    heapq.heappush(card_list, card_1 + card_2)

  print(total)