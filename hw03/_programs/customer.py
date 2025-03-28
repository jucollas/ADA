from sys import stdin
from heapq import heappop, heappush

def greedy(A):
  pqueue, time = [], 0
  for d, p in A:
    time += p
    heappush(pqueue, -p)
    if time > d:
      time += heappop(pqueue)
  return len(pqueue)

def main():
  n_cases = int(stdin.readline().strip())
  while n_cases != 0:
    _black = stdin.readline()
    N = int(stdin.readline().strip())
    orders = []
    for i in range(N):
      q, d = map(int, stdin.readline().split())
      if q <= d:
        orders.append((d, q))
    orders.sort()
    ans = greedy(orders)
    print(ans)
    if n_cases != 1:
      print()

    n_cases -= 1

main()