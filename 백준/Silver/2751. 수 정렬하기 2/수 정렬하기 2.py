import sys
input = sys.stdin.readline

input_count = int(input())

num_list = [int(input()) for _ in range(input_count)]

buff = [None] * len(num_list)

def merge_sort(lst, left, right):
  if left < right:
    center = (left + right) // 2
    
    merge_sort(lst, left, center)
    merge_sort(lst, center+1, right)

    p = j = 0
    i = k = left


    while i <= center:
      buff[p] = num_list[i]
      p += 1
      i += 1

    while i <= right and j < p:
      if buff[j] <= num_list[i]:
        num_list[k] = buff[j]
        j += 1
      
      else:
        num_list[k] = num_list[i]
        i += 1
      
      k += 1
    
    while j < p:
      num_list[k] = buff[j]
      k += 1
      j += 1



merge_sort(num_list, 0, len(num_list)-1)

for i in range(input_count):
  print(num_list[i])