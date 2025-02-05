"""
File: Cantor Solution
Author: Juan Diego Collazos
Date: 1/31/25
"""
from sys import stdin

eps = 1e-14

def trisection(x, a, b):
  ans = True
  low, hi  = a, b
  while abs(hi - low) > eps and ans:
    third = (hi - low) / 3
    md_low = low + third
    md_hi = hi - third
    if md_low <= x < md_hi:
      ans = False
    elif x < md_low:
      hi = md_low
    else:
      low = md_hi
  return ans

def main():
  line = stdin.readline().strip()
  while line != 'END':
    x = float(line)
    ans = trisection(x, 0, 1)
    if ans:
      print('MEMBER')
    else:
      print('NON-MEMBER')
    
    line = stdin.readline().strip()

main()
