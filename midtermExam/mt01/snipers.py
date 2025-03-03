"""
File: Snipers Solution
Author: Juan Diego Collazos
Date: 5/2/25
"""
from sys import stdin
from math import sqrt

k, N, S, D = 0, 0, 0, 0
square_d = 0
soldiers = []

def bisection(f, v, a, b):
  ans = -1
  low, hi  = a, b
  while low <= hi:
    mid = (hi + low) // 2
    if v >= f(mid):
      ans = mid
      low = mid + 1
    else: 
      hi = mid - 1
  return ans

def d(a, b):
  return abs(a - b)

def is_possible_to_cover(v):
  range_of_execution = []
  for xi, yi in soldiers:
    x_dist = int(sqrt(square_d - d(yi, k - v)**2))
    range_of_execution.append((xi - x_dist, xi + x_dist))

  count = index = 1
  current_end = range_of_execution[0][1]
  while index < N and count <= S:
    start, end = range_of_execution[index]
    if start > current_end:
      count += 1
      current_end = end
    else:
      current_end = min(current_end, end)
    index += 1
    
  return count


def main():
  global k, N, S, D, soldiers, square_d
  i, n = 0, int(stdin.readline().strip())
  while i < n:
    _black = stdin.readline()
    k, N, S, D = map(int, stdin.readline().split())
    soldiers, max_soldier = [], float('-inf')
    for _ in range(N):
      x, y = map(int, stdin.readline().split())
      soldiers.append((x, y))
      max_soldier = max(max_soldier, y)

    max_dist_k = d(max_soldier, k)
    if max_dist_k > D:
      ans = -1
    else:
      soldiers.sort()
      square_d = D**2
      ans = bisection(is_possible_to_cover, S, 0, D - max_dist_k)

    print("Case %d: " %(i + 1), end='')
    if ans != -1:
      print(ans)
    else:
      print('IMPOSSIBLE')
    i += 1

main()