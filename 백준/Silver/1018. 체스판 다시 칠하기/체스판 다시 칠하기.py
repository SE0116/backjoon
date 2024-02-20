import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(N)]

cnt = []

for i in range(N - 7):
    for j in range(M - 7):
        W, B = 0, 0
        
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (l + k) % 2 == 0:
                    if graph[k][l] != 'W':
                        W += 1
                    else:
                        B += 1
                else:
                    if graph[k][l] != 'B':
                        W += 1
                    else:
                        B += 1
        cnt.append(W)
        cnt.append(B)

print(min(cnt))