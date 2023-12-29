import sys
input = sys.stdin.readline


# 연속된 히든 넘버 구하기
def getNum(lst, idx):
  num = ''
  for i in range(idx, len(lst)):
    if lst[i] in num_list:
      num += lst[i]
      visited[i] = True
    else:
      break
  return num 


n = int(input())

word = list(map(str, input().strip()))
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

result = []
visited = [False] * (n + 1)
total = 0

# 히든 넘버 구하기
for i in range(len(word)):
  if word[i] in num_list and not visited[i]:
    result.append(getNum(word, i))

# 히든 넘버의 합 구하기
for num in result:
  total += int(num)

print(total)