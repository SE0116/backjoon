# 소수 판별
def is_prime(num):
  if num == 2: return True
  for idx in range(2, int(num**(1/2)+1)):
    if num % idx == 0:
      return False
  return True

input_case_num = int(input())
left, right = [], []

for i in range(input_case_num):
  input_goldbach = int(input())

  # 입력받은 수를 2로 나눈 값을 기준으로 소수가 있는지 역순 탐색
  for idx in range(input_goldbach//2, 1, -1):
    if is_prime(idx):
      if is_prime(input_goldbach-idx):
        left += [idx]
        right += [input_goldbach-idx]
        break


for idx in range(input_case_num):
  print(left[idx], end=' ')
  print(right[idx])