import sys
input = sys.stdin.readline


n = int(input())

triangle = []

for _ in range(n):
  triangle.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(i+1):

    # 맨 왼쪽의 수
    if j==0:
      triangle[i][j] += triangle[i-1][j]

    # 맨 오른쪽의 수
    elif i == j:
      triangle[i][j] += triangle[i-1][j-1]

    # 둘 다 아니면 대각선 왼쪽과 대각선 오른쪽의 값을 더한 것 중 큰 수로
    else:
      triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
 
print(max(triangle[n-1]))