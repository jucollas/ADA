
from sys import stdin

MAX = 20
ans = False
tab = [0 for i  in range(MAX)]
n = 0

def check(k, v):
  for 

def backtrack(i, A):
  global ans
  if i == n:
    ans = True
  else:
    for v in A:
      if check(i, v):
        tab[i] = v
        backtrack(i, A - {v})

def main():
  global n
  n = int(stdin.readline().strip())
  A = set(range(n))
  backtrack(0, A)