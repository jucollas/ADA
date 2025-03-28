from sys import stdin
from math import log2, ceil

def phi(r, l, h):
  if r == l:
    ans = []
  elif r == l - 1:
    ans = [ r ]
  else:
    md = max(r, l - int(2**h))
    ans = [ md ] + phi(r, md, h - 1) + phi(md + 1, l, h - 1)
  return ans

def main():
  i = 1
  N, H = map(int, stdin.readline().split())
  while N != 0:
    print("Case %d: " %(i), end='')
    if N > 2**H - 1:
      print('Impossible.')
    else:
      h = ceil(log2(N + 1))
      if 1 < min(H - h, N) + 1:
        print(' '.join(map(str, range(1, min(H - h, N) + 1))), end=' ')
      if H - h + 1 < N:  
        ans = phi(H - h + 1, N + 1, h - 1)
        print(' '.join(map(str, ans)))

    N, H = map(int, stdin.readline().split())
    i += 1

main()