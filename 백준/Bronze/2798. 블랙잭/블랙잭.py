import sys
input = sys.stdin.readline


N, M = map(int, input().split())

cards = list(map(int,  input().split()))
blackjack = 0

# 카드를 세 묶음으로 한 번 씩 비교해보기
for i in range(N - 2):
  for j in range(i + 1, N - 1):
    for k in range(j + 1, N):
      compare = cards[i] + cards[j] + cards[k]
      if compare <= M and compare > blackjack:
        blackjack = compare

print(blackjack)