import sys
input = sys.stdin.readline


N = int(input())

rope = []
for _ in range(N):
  rope.append(int(input()))

rope.sort()
result = rope[0] * N

for i in range(1, N):
  if rope[i] * (N-i) > result:
    result = rope[i] * (N-i)

print(result)