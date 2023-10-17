import sys
input = sys.stdin.readline

stack_list = []
result = []
command_cnt = int(input())

def is_empty(lst):
  if len(lst) == 0:
    return 1
  return 0


for i in range(command_cnt):
  command_list = input().split()
  
  if command_list[0] == 'push':
    stack_list.append(command_list[1])

  elif command_list[0] == 'pop':
    if len(stack_list) == 0:
      print(-1)
    else:
      print(stack_list.pop())

  elif command_list[0] == 'size':
    print(len(stack_list))

  elif command_list[0] == 'empty':
    print(is_empty(stack_list))

  elif command_list[0] == 'top':
    if len(stack_list) == 0:
      print(-1)
    else:
      print(stack_list[-1])