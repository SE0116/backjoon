import sys
input = sys.stdin.readline

# '-'가 나오면 뒤의 계산은 전부 빼기
minus = input().strip().split('-')
total = 0

# '-'가 나오기 전까지 전부 더하기
for i in minus[0].split('+'):
  total += int(i)

# '+'가 들어간 항에서 숫자를 하나씩 빼서 뺄셈
for i in minus[1:]:
  for j in i.split('+'):
    total -= int(j)

print(total)
