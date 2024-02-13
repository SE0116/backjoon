import heapq
import sys
input = sys.stdin.readline

N = int(input())

max_queue, min_queue = [], []

for i in range(N):
    num = int(input())
    if len(max_queue) == len(min_queue):
        heapq.heappush(max_queue, -num)
    else:
        heapq.heappush(min_queue, num)

    if len(max_queue) >= 1 and len(min_queue) >= 1 and max_queue[0] * -1 > min_queue[0]:
        max_value = heapq.heappop(max_queue) * -1
        min_value = heapq.heappop(min_queue)
        
        heapq.heappush(max_queue, min_value * -1)
        heapq.heappush(min_queue, max_value)

    print(max_queue[0] * -1)