import sys
input = sys.stdin.readline


N = int(input())

book = []
cnt = {}
for _ in range(N):
  book.append(input().strip())

book.sort()
for name in book:
  if name not in cnt:
    cnt[name] = 0

  cnt[name] += 1

cnt = sorted(cnt.items(), key = lambda x: x[1], reverse=True)

print(cnt[0][0])