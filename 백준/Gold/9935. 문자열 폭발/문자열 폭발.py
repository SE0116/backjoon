import sys
input = sys.stdin.readline


word = list(input().strip())
bomb = list(input().strip())

stack = []

# 스택에 하나씩 추가하면서 폭탄이 생기는지 확인
for i in range(len(word)):
  stack.append(word[i])
  if stack[-(len(bomb)):] == bomb:
    for _ in range(len(bomb)):
      stack.pop()

# 터지지 않은 글자가 있으면 출력
if stack:
  print(*stack, sep='')
# 전부 터졌으면 FRULA 출력
else:
  print('FRULA')