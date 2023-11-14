from collections import deque
import sys
input = sys.stdin.readline


board = deque(list(input().strip()))

check = 0
result = deque()

while board:
  letter = board.popleft()
  
  if letter == 'X':
    check += 1
  
  if letter == '.':
    if check % 2:
      print(-1)
      break
    else:
      if check % 4 == 0:
        for _ in range(check//4):
          result.append('AAAA')

      else:
        for _ in range(check//4):
          result.append('AAAA')
        result.append('BB')
        
    check = 0
    result.append('.')
else:
  if check % 4 == 0:
    for _ in range(check//4):
      result.append('AAAA')

  elif check % 2 == 0:
    for _ in range(check//4):
      result.append('AAAA')
    result.append('BB')
  else:
    result = deque('-1')
  print(''.join(result))