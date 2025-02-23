"""
File: Artic Virus Solution
Author: Juan Diego Collazos
Date: 2/19/25
"""
from sys import stdin

A = str()
dp = dict()

def phi(l, r):
  if (l, r) in dp:
    ans = dp[l, r]
  else:
    ans = False
    if abs(l - r) == 0:
      ans = A[l] == 'A' or A[l] == 'T'
    else:
      sign = 1 if l < r else -1
      if A[r] == 'C':
        ans = phi(l, r - sign)
        if A[l] == 'G' and abs(l - r) > 1:
            ans = ans or phi(r - sign, l + sign)
      if A[l] == 'A':
        ans = ans or phi(l + sign, r) or phi(r, l + sign)
    dp[l, r] = ans
  return ans

def main():
  global A, dp
  line = stdin.readline()
  while line:
    n, A = line.split()
    N = int(n)
    if phi(0, N - 1):
      if len(A) == 1:
        print("simple")
      else:
        print("mutation")
    else:
      print("doomed")
    dp.clear()
    line = stdin.readline()

main()