import sys
from collections import deque

input = sys.stdin.readline

queue = deque([])
command_cnt = int(input())

def is_empty(lst):
  if len(lst) == 0:
    return 1
  return 0


for i in range(command_cnt):
  command_list = input().split()
  
  if command_list[0] == 'push':
    queue.append(command_list[1])

  elif command_list[0] == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.popleft())

  elif command_list[0] == 'size':
    print(len(queue))

  elif command_list[0] == 'empty':
    print(is_empty(queue))

  elif command_list[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])

  elif command_list[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])