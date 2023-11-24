import sys
input = sys.stdin.readline


N = int(input())

card_one = list(map(int, input().split()))

M = int(input())

card_two = list(map(int, input().split()))

card_dict = {}

for num in card_one:
  if num not in card_dict:
    card_dict[num] = 0
  card_dict[num] += 1

for num in card_two:
  if num not in card_dict:
    print(0, end=' ')
  else:
    print(card_dict[num], end=' ')