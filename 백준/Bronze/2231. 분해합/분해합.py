import sys
input = sys.stdin.readline


N = int(input())

sum_list = [0] * (N + 1)

for i in range(1, N + 1):
  total = 0

  if not i // 10:
    total = i + i

  elif not i // 100:
    total = i + (i // 10) + (i % 10)
  
  elif not i // 1000:
    total = i + (i // 100) + (i % 100 // 10) + (i % 10)
  
  elif not i // 10000:
    total = i + (i // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10)

  elif not i // 100000:
      total = i + (i // 10000) + (i % 10000 // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10)

  elif not i // 1000000:
      total = i + (i // 100000) + (i % 100000 // 10000) + (i % 10000 // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10)

  else:
     total = 1000001

  if total > N or sum_list[total]:
    continue

  sum_list[total] = i

print(sum_list[N])