'''
File: Interesting Drink Solution
Author: Juan Diego Collazos
Date: 1/31/25
'''
from sys import stdin

def lower_bound(A, v):
  low, hi = 0, len(A)
  while hi - low > 1:
    mid = low + (hi -  low >> 1)
    if v < A[mid]:
      hi = mid
    else:
      low = mid
  ans = low if v < A[low] else hi
  return ans

def main():
  line = stdin.readline()
  while len(line) != 0:
    _ = int(line.strip())
    prices_bottles = list(map(int, stdin.readline().split()))
    prices_bottles.sort()

    q = int(stdin.readline().strip())
    for _ in range(q):
      m = int(stdin.readline().strip())
      ans = lower_bound(prices_bottles, m)
      print(ans)
    line = stdin.readline()
    
main()
