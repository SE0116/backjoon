import sys
input = sys.stdin.readline

N = int(input())

moneys = [500, 100, 50, 10, 5, 1]
rest = 1000 - N
result = 0

for money in moneys:
    if rest == 0:
        break
    
    result += rest // money
    rest %= money
    
print(result)