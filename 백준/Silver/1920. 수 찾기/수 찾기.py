def binary_search(lst, num):
  left, right = 0, len(lst)-1

  while left <= right:
    center = (left + right) // 2
    if lst[center] == num:
      return True
    elif lst[center] < num:
      left = center+1
    else:
      right = center-1
  return False


first = int(input())
first_list = sorted(list(map(int, input().split())))
second = int(input())
second_list = list(map(int, input().split()))

for i in range(second):
  if binary_search(first_list, second_list[i]):
    print(1)
  else:
    print(0)