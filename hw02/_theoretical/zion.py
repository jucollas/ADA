
dp = dict()

def phi(i, t):
  if (i, t) in dp:
    ans = dp[i, t]
  else:
    if t == 0:
      ans = 0
    else:
      ans = phi(0, t - 1) + min(X[i], F[i])
      if i < N - 1:
        ans = max(ans, phi(i + 1, t - 1))
    dp[i, t] = ans
  return ans

X = [1, 10, 10, 1]
F = [1, 2, 4, 8]
N = len(F)

T = 4
ans = phi(0, T)
print(ans)
