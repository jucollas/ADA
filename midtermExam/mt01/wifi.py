"""
File: WiFi Solution
Author: Juan Diego Collazos
Date: 3/2/25
"""
from sys import stdin

eps = 1e-1
street = []
n = 0

def is_posible(x):
  i, cnt, router = 1, 1, street[0] + x
  while i < len(street) and cnt <= n:
    if abs(street[i] - router) > x:
      router = street[i] + x
      cnt += 1
    i += 1
  return cnt <= n

def bisection(f, a, b):
  low, hi  = a, b
  while abs(hi - low) > eps:
    mid = (hi + low) / 2
    if f(mid): hi = mid
    else: low = mid
  ans = low
  return ans

def main():
  global street, n
  n_cases = int(stdin.readline().strip())
  while n_cases != 0:
    n, m = map(int, stdin.readline().split())
    street = []
    for i in range(m):
      street.append(int(stdin.readline().strip()))
    street.sort()
    ans = bisection(is_posible, 0, street[-1])
    print("%.1f" %(ans))
    n_cases -= 1 

main()