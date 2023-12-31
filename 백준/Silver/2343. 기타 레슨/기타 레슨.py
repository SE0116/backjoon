import sys
input = sys.stdin.readline


N, M = map(int, input().split())

guitar = list(map(int, input().split()))

start = max(guitar)
end = sum(guitar)

while start <= end:
    mid = (start + end) // 2 
    total, cnt = 0, 1
    
    for length in guitar:
        if total + length > mid:
            cnt += 1
            total = 0
        total += length 

    if cnt <= M:
        result = mid
        end = mid - 1

    else:
        start = mid + 1
    
print(result)