import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
  x = int(input())
  if x == 0:
    if not heap:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap,x)
