from sys import stdin

MAX = 30
POWERS_TWO = []

def precompute():
  acum = 1
  for i in range(MAX + 1):
    POWERS_TWO.append(acum)
    acum *= 2

def phi(r, l, h):
  if r == l - 1:
    ans = [ r ]
  else:
    md = max(r, l - POWERS_TWO[h])
    ans = [ md ]
    calls = [(r, md), (md + 1, l)]
    for ri, li in calls:
      if ri != li:
        ans.extend(phi(ri, li, h - 1))
  return ans

def main():
  i = 1
  N, H = map(int, stdin.readline().split())
  while N != 0:
    print("Case %d: " %(i), end='')
    if N > POWERS_TWO[H] - 1:
      print('Impossible.')
    else:
      ans = phi(1, N + 1, H - 1)
      print(' '.join(map(str, ans)))
    N, H = map(int, stdin.readline().split())
    i += 1

precompute()
main()