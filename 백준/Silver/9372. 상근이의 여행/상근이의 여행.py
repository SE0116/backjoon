import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  
  airplane = [[] for _ in range(N + 1)]
  parents = [0] * (N + 1)
  for _ in range(M):
    a, b = map(int, input().split())

  # 원하는 출력 값이 타야 하는 비행기의 갯수가 아닌 비행기 종류의 갯수이므로 단순히 N-1만 해도 정답
  print(N-1)