from sys import stdin

MAX = 9
sudo = [[0 for i in range(MAX)] for i in range(MAX)]

def check(x, y, v):
  ans = True
  sudo[x][y] = -1
  i = 0
  while i < MAX and ans:
    if v == sudo[i][y] or v == sudo[x][i]:
      ans = False
    i += 1

  xx, yy = (x // 3) * 3, (y // 3) * 3
  i = xx
  while i < xx + 3  and ans:
    j = y
    while j < yy + 3 and ans:
      if v == sudo[x][y]:
        ans = False
      j += 1
    i += 1
  return ans

ans = False

def backtrack(x, y):
  global ans
  if y == 9:
    ans = True
  else:
    if x == 9:
      ans = backtrack(0, y + 1)
    else:
      if sudo[x][y] != 0:
        if check(x, y, sudo[x][y]):
          ans = backtrack(x, y + 1)
      else:
        v = 1
        while v <= MAX and not ans:
          if check(x, y, v):
            sudo[x][y] = v
            ans = backtrack(x + 1, y)
          v += 1

def main():
  for i in range(MAX):
    row = stdin.readline().strip()
    for cel in row:
      sudo.append(int(cel))
  ans = backtrack(0, 0)
  if ans:
    print("YES")
    print(sudo)
  else:
    print('NO')

main()

  
