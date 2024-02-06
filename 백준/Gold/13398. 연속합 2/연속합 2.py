import sys
input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))
dp_list = [[i for i in num_list] for _ in range(2)]

for i in range(1, N):
    dp_list[0][i] = max(dp_list[0][i - 1] + num_list[i], dp_list[0][i])
    dp_list[1][i] = max(dp_list[0][i - 1], dp_list[1][i - 1] + num_list[i])

print(max(max(dp_list[0]), max(dp_list[1])))