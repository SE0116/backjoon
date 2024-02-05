import sys
input = sys.stdin.readline

MOD = 1000000003
        
N = int(input())
K = int(input())

dp_list = [[0] * (N + 1) for i in range(N + 1)]

for i in range(N + 1):
    dp_list[i][0], dp_list[i][1] = 1, i

for i in range(3, N + 1):
    for j in range(2, int((i + 1) / 2) + 1):
        dp_list[i][j] = (dp_list[i - 1][j] + dp_list[i - 2][j - 1]) % MOD

print((dp_list[N - 3][K - 1] + dp_list[N - 1][K]) % MOD)