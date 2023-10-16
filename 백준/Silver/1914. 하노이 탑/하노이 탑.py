def move(no, x, y, path):
    if no == 1:
        path.append((x, y))
    else:
        move(no - 1, x, 6 - x - y, path)
        if no <= 20:
            path.append((x, y))
        move(no - 1, 6 - x - y, y, path)

n = int(input())
if n > 20:
    print(2**n-1)
else:
  move_path = []
  move(n, 1, 3, move_path)

  print(len(move_path))
  if n <= 20:
      for move_step in move_path:
          print(f'{move_step[0]} {move_step[1]}')
