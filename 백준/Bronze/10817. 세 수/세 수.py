import sys
input = sys.stdin.readline


ABC = list(map(int, input().split()))
ABC.sort()
print(ABC[1])