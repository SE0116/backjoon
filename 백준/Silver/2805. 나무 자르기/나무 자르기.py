import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree_list = list(map(int, input().split()))

start, end = 0, max(tree_list)

while start <= end :
    mid = (start + end) // 2
    total = 0
    
    for tree in tree_list :
        if tree > mid :
            total += tree - mid
            
    if total >= M:
        start = mid + 1
    else :
        end = mid - 1
        
print(end)