import sys
input = sys.stdin.readline

# 16진수의 알파벳 숫자로 변경
def isAlpha(num):
  if num == 'a':
    num = 10
  elif num == 'b':
    num = 11
  elif num == 'c':
    num = 12
  elif num == 'd':
    num = 13
  elif num == 'e':
    num = 14
  elif num == 'f':
    num = 15
  return num

num = input()
X = list(map(str, num.strip()))

result = 0

# 10진수가 아닐 때
if X[0] == '0':

  # 16진수일 때
  if X[1] == 'x':
    X = X[2:]
    cnt = 0
    for x in X[-1:-(len(X)+1):-1]:
      x = isAlpha(x)
      result += int(x)*(16**cnt)
      cnt += 1

  # 8진수일 때
  else:
    X = X[1:]
    cnt = 0
    for x in X[-1:-(len(X)+1):-1]:
      result += int(x)*(8**cnt)
      cnt += 1

# 10진수일 때
else:
  result = int(num)

print(result)