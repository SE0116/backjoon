input_circle_size = int(input())

def hanoi(size, start, end):
  if size > 1:
    hanoi(size-1, start, 6-start-end)
  
  global move
  move += 1
  
  if input_circle_size <= 20:
    global from_start, to_end
    from_start += [start]
    to_end += [end]


  if size > 1:
    hanoi(size-1, 6-start-end, end)


if input_circle_size > 20:
  print(2**input_circle_size - 1)
else:
  global move, from_start, to_end
  move, from_start, to_end = 0, [], []



  hanoi(input_circle_size, 1, 3)

  print(move)
  if input_circle_size <= 20:
    for idx in range(move):
      print(from_start[idx], to_end[idx])