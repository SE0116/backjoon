input_count = int(input())

num_list = [int(input()) for _ in range(input_count)]

result = sorted(num_list)

for i in range(input_count):
  print(result[i])