import sys
input = sys.stdin.readline


cnt_A, cnt_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A - B) + len(B - A))