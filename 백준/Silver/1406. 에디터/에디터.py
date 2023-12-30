import sys
input = sys.stdin.readline


word = list(map(str, input().strip()))

M = int(input())

stack = []

for _ in range(M):
  command = list(map(str, input().split()))

  if command[0] == 'L':
    if word:
      stack.append(word.pop())

  elif command[0] == 'D':
    if stack:
      word.append(stack.pop())

  elif command[0] == 'B':
    if word:
      word.pop()
  
  else:
    word.append(command[1])

word.extend(reversed(stack))

print(*word, sep='')