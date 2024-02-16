import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T) :
    n = int(input())
    
    dp_list = [list(map(int, input().split())) for _ in range(2)]

    if n > 1 :
        dp_list[0][1] += dp_list[1][0]
        dp_list[1][1] += dp_list[0][0]
    for i in range(2, n) :
        dp_list[0][i] += max(dp_list[1][i-1], dp_list[1][i-2])
        dp_list[1][i] += max(dp_list[0][i-1], dp_list[0][i-2])

    print(max(dp_list[0][n-1], dp_list[1][n-1]))