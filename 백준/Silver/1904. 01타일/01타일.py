import sys
input = sys.stdin.readline

N = int(input())

binary_list = [0] * (N+1)

binary_list[0] = 0
binary_list[1] = 1
if N >=2 :
  binary_list[2] = 2

for i in range(3, N+1):
  binary_list[i] = (binary_list[i-1] + binary_list[i-2]) % 15746

print(binary_list[N])