import sys
input = sys.stdin.readline

str_1 = input().strip()
str_2 = input().strip()

dp_list = [[0] * (len(str_2) + 1) for _ in range(len(str_1) + 1)]

for i in range(1, len(str_1) + 1):
  for j in range(1, len(str_2) + 1):

    if str_1[i-1] == str_2[j-1]:
      dp_list[i][j] = dp_list[i-1][j-1] + 1

    else:
      dp_list[i][j] = max(dp_list[i-1][j], dp_list[i][j-1])

print(dp_list[-1][-1])