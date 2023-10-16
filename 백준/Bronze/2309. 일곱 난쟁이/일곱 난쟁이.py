import sys
input = sys.stdin.readline

height_list = sorted([int(input()) for _ in range(9)])

height_sum = 0
trick = []
for i in range(len(height_list)):
  height_sum += height_list[i]

# 가짜 난쟁이를 찾아 인덱스 저장
for i in range(len(height_list)-1):
  if len(trick) == 2:
    break
  for j in range(i+1, len(height_list)):
    if height_sum - (height_list[i] + height_list[j]) == 100:
      trick += [i, j]
      break

# 일곱 난쟁이 키 출력
for i in range(len(height_list)):
  if i in trick:
    continue
  print(height_list[i])