import sys
input = sys.stdin.readline

len_square = int(input())

color_list = [list(map(int, input().split())) for _ in range(len_square)]

white, blue = 0, 0
def square(lst):
  global white, blue
  
  if len(lst) == 1:
    if lst[0][0] == 1:
      blue += 1
    else:
      white += 1
    return

  if check_color(lst):
    if lst[0][0] == 1:
      blue += 1
    else:
      white += 1
  else:
    square([lst2[:len(lst)//2] for lst2 in lst[:len(lst[0])//2]])
    square([lst2[len(lst)//2:] for lst2 in lst[:len(lst[0])//2]])
    square([lst2[:len(lst)//2] for lst2 in lst[len(lst[0])//2:]])
    square([lst2[len(lst)//2:] for lst2 in lst[len(lst[0])//2:]])
  return
    


def check_color(lst):
  b, w = 0, 0
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j] == 1:
        b += 1
      else: w += 1
  if len(lst) * len(lst[0]) == b or len(lst) * len(lst[0]) == w:
    return True
  return False
  
square(color_list)

print(white, blue, sep='\n')