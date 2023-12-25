self_num = [True] * 10001
for num in range(1, 10001):
  # 셀프 넘버일 때만 출력
  # 해당 수의 순서가 되기 전에 생성자가 안됐으면 셀프 넘버로 간주
  if self_num[num]:
    print(num)

  # num < 10
  if not num // 10:
    self_num[num * 2] = False
  
  # 10 <= num < 100
  elif not num // 100:
    self_num[num + (num // 10) + (num % 10)] = False
    
  # 100 <= num < 1000
  elif not num // 1000:
    self_num[num + (num // 100) + (num % 100 // 10) + (num % 10)] = False

  # 1000 <= num < 10000
  elif not num // 10000:
    # 인덱스 에러를 방지하기 위해 생성자가 10000이 넘으면 셀프넘버 계산 X
    check = num + (num // 1000) + (num % 1000 // 100) + (num % 100 // 10) + (num % 10)
    if check > 10000:
      continue
    self_num[check] = False