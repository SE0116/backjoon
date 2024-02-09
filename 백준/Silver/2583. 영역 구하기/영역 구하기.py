from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]


def bfs(i, j):
    q = deque()
    q.append((i, j))

    cnt = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            y_dy = y+dy[k]
            x_dx = x+dx[k]
            if (0 <= y_dy < M) and (0 <= x_dx < N) and graph[y_dy][x_dx] == 0:
                graph[y_dy][x_dx] = 1
                q.append((y_dy, x_dx))
                cnt += 1
    return cnt


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

result = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))