'''
Substring maximo
'''
from sys import stdin

A = B = str()
dp = dict()

def fi(i, j):
  if (i, j) in dp:
    ans = dp[i, j]
  else:
    if i == len(A) or j == len(B):
      ans = 0
    elif A[i] == B[j]:
      ans = 1 + fi(i + 1, j + 1)
    else:
      ans = max(fi(i + 1,  j), fi(i, j + 1))
    dp[i, j] = ans
  return ans

A = "QWERTVYU"
B = "ASDFGHJQWERTYU"
print(fi(0, 0))


